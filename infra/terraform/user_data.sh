#!/bin/bash
set -euxo pipefail

dnf update -y
dnf install -y git python3 python3-pip

mkdir -p /opt/trade-bot
chown ec2-user:ec2-user /opt/trade-bot
