module "VPC" {
    source = "../modules/VPC"
    vpc_cidr = var.vpc_cidr
    private_subnets = var.private_subnets
    public_subnets = var.public_subnets
}

module "SecurityGroup" {
    source = "../modules/SecurityGroup"
    vpc_id = module.VPC.vpc_id
}

module "IAM" {
    source = "../modules/IAM"
}

module "EKS" {
    source = "../modules/EKS"
    cluster_name = var.cluster_name
    eks_version = var.eks_version
    eks_cluster_role_arn = module.IAM.eks_cluster_role_arn
    private_subnet_ids = module.VPC.private_subnet_ids
    eks_cluster_sg_id = module.SecurityGroup.eks_cluster_sg_id
    depends_on = [ module.VPC ]
}

module "NodeGroup" {
    source = "../modules/NodeGroup"
    cluster_name = var.cluster_name
    eks_node_group_role_arn = module.IAM.eks_node_group_role_arn
    private_subnet_ids = module.VPC.private_subnet_ids
    depends_on = [ module.EKS ]
}

module "Bastion" {
    source = "../modules/Bastion"
    vpc_id = module.VPC.vpc_id
    public_subnet_ids = module.VPC.public_subnet_ids
    bastion_sg_id = module.SecurityGroup.bastion_sg_id
    depends_on = [ module.EKS ]
}

module "DocumentDB" {
    source = "../modules/DocumentDB"
    private_subnet_ids = module.VPC.private_subnet_ids
    docdb_sg_id = module.SecurityGroup.docdb_sg_id
    dev_docdb_username = var.dev_docdb_username
    dev_docdb_password = var.dev_docdb_password
    stage_docdb_username = var.stage_docdb_username
    stage_docdb_password = var.stage_docdb_password
    prod_docdb_username = var.prod_docdb_username
    prod_docdb_password = var.prod_docdb_password
    depends_on = [ module.VPC, module.SecurityGroup ]
}