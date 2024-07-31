output "eks_cluster_sg_id" {
    value = aws_security_group.eks_cluster_sg.id
}

output "bastion_sg_id" {
    value = aws_security_group.bastion_sg.id
}

output "docdb_sg_id" {
    value = aws_security_group.docdb_sg.id
}
