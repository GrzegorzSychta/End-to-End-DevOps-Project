# TO-DO: Replace with HashiCorp Vault
cluster_name = "FinTrack"
region = "eu-west-2"
vpc_cidr = "10.0.0.0/16"
private_subnets = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
public_subnets = ["10.0.1.0/24"]
eks_version = "1.30"
aws_access_key = ""
aws_secret_key = ""
dev_docdb_username = ""
dev_docdb_password = ""
stage_docdb_username = ""
stage_docdb_password = ""
prod_docdb_username = ""
prod_docdb_password = ""