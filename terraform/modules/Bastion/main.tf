# I decided to use Bastion instance to access the EKS cluster. It's insecure but simplifies the setup. In real life, you should use VPN or AWS Direct Connect.

resource "tls_private_key" "bastion" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "local_file" "private_key" {
  content  = tls_private_key.bastion.private_key_pem
  filename = "${path.module}/bastion_key.pem"
}

resource "local_file" "public_key" {
  content  = tls_private_key.bastion.public_key_openssh
  filename = "${path.module}/bastion_key.pub"
}

resource "aws_key_pair" "bastion_key" {
  key_name   = "bastion_key"
  public_key = tls_private_key.bastion.public_key_openssh
}

resource "aws_instance" "bastion" {
  ami                         = "ami-020737107b4baaa50"
  instance_type               = "t3.micro"
  subnet_id                   = var.public_subnet_ids[0]
  security_groups             = [var.bastion_sg_id]
  key_name                    = aws_key_pair.bastion_key.key_name
  associate_public_ip_address = true
}

