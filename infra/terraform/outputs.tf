output "vpc_id" {
  value = aws_vpc.this.id
}

output "public_subnet_id" {
  value = aws_subnet.public_1a.id
}

output "security_group_id" {
  value = aws_security_group.ec2.id
}

output "instance_id" {
  value = aws_instance.trade_bot.id
}

output "public_ip" {
  value = aws_instance.trade_bot.public_ip
}

output "public_dns" {
  value = aws_instance.trade_bot.public_dns
}

output "ssh_command" {
  value = "ssh -i <private_key_path> ec2-user@${aws_instance.trade_bot.public_ip}"
}
