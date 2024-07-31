resource "aws_eks_cluster" "eks" {
  name = var.cluster_name
  version = var.eks_version
  role_arn = var.eks_cluster_role_arn

  vpc_config {
    subnet_ids = var.private_subnet_ids
    security_group_ids = [var.eks_cluster_sg_id]
    endpoint_private_access = true
    endpoint_public_access = false
  }
}
