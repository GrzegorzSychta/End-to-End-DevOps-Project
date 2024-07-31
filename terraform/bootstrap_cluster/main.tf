module "SealedSecrets" {
    source = "../modules/SealedSecrets"
}

module "ArgoCD" {
    depends_on = [ module.SealedSecrets ]
    source = "../modules/ArgoCD"
}
