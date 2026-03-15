import logging
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.binance.com/api/v3/ticker/price"

SYMBOL = os.getenv("SYMBOL", "BTCUSDT")
BUY_PRICE = float(os.getenv("BUY_PRICE", "70000"))
SELL_PRICE = float(os.getenv("SELL_PRICE", "75000"))
INTERVAL_SEC = int(os.getenv("INTERVAL_SEC", "60"))
LOG_FILE = os.getenv("LOG_FILE", "bot.log")
REQUEST_TIMEOUT_SEC = int(os.getenv("REQUEST_TIMEOUT_SEC", "10"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_WAIT_SEC = int(os.getenv("RETRY_WAIT_SEC", "2"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
session = requests.Session()


def get_price(symbol: str) -> float:
    url = f"{API_URL}?symbol={symbol}"
    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT_SEC)
            response.raise_for_status()
            data = response.json()
            return float(data["price"])

        except Exception as e:
            last_error = e
            logger.warning(
                "price fetch failed attempt=%s/%s symbol=%s error=%s",
                attempt,
                MAX_RETRIES,
                symbol,
                e,
            )

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_WAIT_SEC)

    raise RuntimeError(f"price fetch failed after retries: {last_error}")


def evaluate_signal(price: float, has_position: bool) -> bool:
    if not has_position and price < BUY_PRICE:
        logger.info("BUY SIGNAL price=%.2f", price)
        return True

    if has_position and price > SELL_PRICE:
        logger.info("SELL SIGNAL price=%.2f", price)
        return False

    logger.info("WAIT")
    return has_position


def main() -> None:
    has_position = False

    logger.info(
        "BOT START symbol=%s buy_price=%.2f sell_price=%.2f interval_sec=%s max_retries=%s retry_wait_sec=%s",
        SYMBOL,
        BUY_PRICE,
        SELL_PRICE,
        INTERVAL_SEC,
        MAX_RETRIES,
        RETRY_WAIT_SEC,
    )

    while True:
        try:
            price = get_price(SYMBOL)

            logger.info(
                "symbol=%s price=%.2f has_position=%s",
                SYMBOL,
                price,
                has_position,
            )

            has_position = evaluate_signal(price, has_position)

        except Exception as e:
            logger.exception("bot loop failed: %s", e)

        time.sleep(INTERVAL_SEC)


if __name__ == "__main__":
    main()
