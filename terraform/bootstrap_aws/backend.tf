# Backend for terraform state file.
terraform {
  backend "s3" {
    bucket         = "fintrack-terraform-state-bucket"
    key            = "states/terraform.tfstate"
    region         = "eu-west-2"
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}