# Node Group for application.
resource "aws_eks_node_group" "application_managed_workers" {
  cluster_name    = var.cluster_name
  node_group_name = "application_managed_workers"
  node_role_arn   = var.eks_node_group_role_arn
  subnet_ids      = var.private_subnet_ids
  instance_types  = ["t3.medium"]

  scaling_config {
    desired_size = 2
    max_size     = 5
    min_size     = 2
  }

  update_config {
    max_unavailable = 1
  }

  labels = {
    "node.kubernetes.io/scope" = "application"
  }
}

# Node Group for add-ons like ArgoCD, SealedSecrets, etc.
resource "aws_eks_node_group" "critical_addons" {
  cluster_name    = var.cluster_name
  node_group_name = "critical_addons"
  node_role_arn   = var.eks_node_group_role_arn
  subnet_ids      = var.private_subnet_ids
  instance_types  = ["t3.medium"]

  scaling_config {
    desired_size = 2
    max_size     = 5
    min_size     = 2
  }

  update_config {
    max_unavailable = 1
  }

  taint {
    key    = "CriticalAddonsOnly"
    value  = "true"
    effect = "NO_SCHEDULE"
  }

  labels = {
    "node.kubernetes.io/scope" = "system"
  }
}