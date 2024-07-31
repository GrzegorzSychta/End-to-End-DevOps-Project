resource "aws_docdb_subnet_group" "docdb_subnet_group" {
  name       = "docdb-subnet-group"
  subnet_ids = var.private_subnet_ids
}

resource "aws_docdb_cluster" "dev" {
  cluster_identifier      = "dev-docdb-cluster"
  master_username         = var.dev_docdb_username
  master_password         = var.dev_docdb_password
  backup_retention_period = 1
  preferred_backup_window = "07:00-09:00"
  port = 27017
  skip_final_snapshot = true
  vpc_security_group_ids = [var.docdb_sg_id]
  db_subnet_group_name  = aws_docdb_subnet_group.docdb_subnet_group.name
}

resource "aws_docdb_cluster_instance" "dev_instance" {
  identifier        = "dev-docdb-instance"
  cluster_identifier = aws_docdb_cluster.dev.id
  instance_class     = "db.t4g.medium"
}

resource "aws_docdb_cluster" "stage" {
  cluster_identifier      = "stage-docdb-cluster"
  master_username         = var.stage_docdb_username
  master_password         = var.stage_docdb_password
  backup_retention_period = 1
  preferred_backup_window = "07:00-09:00"
  port = 27017
  skip_final_snapshot = true

  vpc_security_group_ids = [var.docdb_sg_id]
  db_subnet_group_name  = aws_docdb_subnet_group.docdb_subnet_group.name
}

resource "aws_docdb_cluster_instance" "stage_instance" {
  identifier        = "stage-docdb-instance"
  cluster_identifier = aws_docdb_cluster.stage.id
  instance_class     = "db.t4g.medium"
}

resource "aws_docdb_cluster" "prod" {
  cluster_identifier      = "prod-docdb-cluster"
  master_username         = var.prod_docdb_username
  master_password         = var.prod_docdb_password
  backup_retention_period = 3
  preferred_backup_window = "07:00-09:00"
  port = 27017
  skip_final_snapshot = true

  vpc_security_group_ids = [var.docdb_sg_id]
  db_subnet_group_name  = aws_docdb_subnet_group.docdb_subnet_group.name
}

resource "aws_docdb_cluster_instance" "prod_instance" {
  identifier        = "prod-docdb-instance"
  cluster_identifier = aws_docdb_cluster.prod.id
  instance_class     = "db.t4g.medium"
}
