variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "ap-northeast-1"
}

variable "project_name" {
  type        = string
  description = "Project name"
  default     = "trade-bot"
}

variable "environment" {
  type        = string
  description = "Environment name"
  default     = "dev"
}

variable "vpc_cidr" {
  type        = string
  description = "VPC CIDR block"
  default     = "10.10.0.0/16"
}

variable "public_subnet_cidr" {
  type        = string
  description = "Public subnet CIDR block"
  default     = "10.10.1.0/24"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "instance_name" {
  type        = string
  description = "EC2 instance name"
  default     = "trade-bot-ec2"
}

variable "allowed_ssh_cidr_blocks" {
  type        = list(string)
  description = "CIDR blocks allowed to SSH"
}

variable "public_key_path" {
  type        = string
  description = "Path to the local public key file"
}

variable "key_name" {
  type        = string
  description = "EC2 key pair name"
  default     = "trade-bot-key"
}

variable "root_volume_size" {
  type        = number
  description = "Root EBS volume size in GiB"
  default     = 20
}
