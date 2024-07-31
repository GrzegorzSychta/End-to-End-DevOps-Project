resource "kubernetes_namespace" "argocd" {
  metadata {
    name = "argocd"
  }
}

# I used the following command to apply the Sealed Secret.

resource "null_resource" "sealed_secrets_key" {
  depends_on = [kubernetes_namespace.argocd]

  provisioner "local-exec" {
    command = <<EOT
      kubectl apply -f - <<EOF
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  annotations:
    sealedsecrets.bitnami.com/cluster-wide: "true"
  creationTimestamp: null
  name: github-argocd-repo
  namespace: argocd
spec:
  encryptedData:
    insecure: AQAw9BH9fGRvVFQ3oHOBG3SbLcBzS/nNG48T0VQEct1ey7f+V9XAqeG1j08GQ6sQ9SNebK4BDLJ5Zss7wxaURbTvoK9d6tJGq+0wdtmL2K/MTQx4ayHFazE1PqmzYGtWAAcM3N/5MyzT9xTyJtqaNN168MtudXmrklltUcBFCsqV9aq2UHKPFqeJCECw5xT6mLxc5W9PSuHv3gysAeYZIVoF0dg38N+labWxBBX6V+w8a5um5V6oKLoI8/VdizQNGGVmi7F0JsOjDU99NJkOvNCu5dZIU1EYE5P8QAQy0R/0g02LWOYcJpElW/BdCf/R17UwQsQzapgDKs8zis9GARHENgVYkQx38246jXxvoj2llbPa0JA=
    password: AQCNs2bTeRIwc16m+ols6HZQlUAB3NBAO9Zxacnh3UT40sNQ7Zu8xFl23EjLiOLezGANNYtK9uNV/lUuXeogPuGLRMPKqHBJO2vWQKvaHiGX91PVasrAb9ElqUnI2ggUwJBCmRyC2b6gX4hBH3SAsDqpxALw7Rd71kG6bO0KtJ0GJQMghaoahE6wbuMfoJRu6tXh1Jfmua/5CwIN+uD1HYBLq1N+6vMIwb+eHs3mQ2Y7ATC3YuPNxEcQtHjDjo7HG37AZSbOUS7qiR8j0NJ3wKx6lhz/5yi351G7MLyK84qLiwmEa21nv6KGuTiO0EFVVkDzB84aEXBGbhwzYv55I3Ves8dJLmQgoCCj1OUxi2FJwuXqMEv8rvxhIVCYYDgDYbVYTNqUXyF3O7G2ZeU8u6e3EEK9SVSDoig=
    type: AQB8X4zoaoW5dD6TpiBzaQ9puCSpY/pjSki4qs6zyH7l37na/6+4aSb3rPaLIFokbPgXPjrotSNVY+nNJmKFc6meHCsOxsJxJSRSolvtaQ9yQDJoymktKTw4wg8BAu0dByU6iEWTRkb2ArOID1sxWeILb47hxoY6uF4dtGOBuoqPgCePToRZWBo8O+5DBhVrYyscgI42oywjTHZwDDBNlwj6K2/uEBPk4EvWAvIogeGtad/sHGCJkDnUlWtG0OuvW0TbE9XSEC2KC1KAe9Ixc/jCP79Z+dnSizWNz8XyQjA87Vg+8QSKLBIV7CBgrPxmpMH+ArrXKjwit8AZxZfEV4mLaWaiBa8XQK5FJZVdU27qUwQhsA==
    url: AQCYlNqkPD+1JYehM8O4WQI5repC6ovPeaNMubIrConmeL3m+Zo4itKJO3sJIgAXaZPrPGgxTIYAuhK0oIzqWzS4RoUQxfAihWJFxyM4wWpsaWbU63y8vhoVnT6Lwd/zyxdnpCZqkjacvr4iu9tZBV2tZaVAXWrV7oy8aKWHEMlHmhk2jyRhtRUgTFfbMNbYR0nMo89cUSOOXsxxM830Me6Siqbq4Ez7fq2rSh0xI1DM3QM0VZ8hErVIbeVhX7x6zJnY+H6tNBjlXoBpoJ0Bfa8gunZ00J/tbB54HiI3X6UlKv1plzX51W1yUGfXSp58xQBwUPqZRRrJ8xE17jHdJBjOzhxWQsKH4woXBzMzbhPAkRELPVniPhBQ4FSo3DCr9scot8JdLd5SMaL+NDOOwCF8d9FJtNsqCmNo6Q==
    username: AQB4AUsia++6YD9TrW2Fm0aRs+rXkx/FBDh2Pf58HIh7bvCVCkYEE9egnnfiWQyQsk39ei1Vp00mNvcAgglbDclNL7yqJfr2/NqtChuvG51cDxqz9cL0LkRKQd9XrcKWDULfKCsqQ7dIuHgDEgm30i2zqIXj3dey5V2zx2Zvjq03oCoVELTT+70AEIV7dsY1B8tYbsNNO0OuAuDyaZLj6oYqx1RtVlC8m6JCoRQfCIAaUtU5V+Amfci9kPpF4YiqHIhtV+WSK0C7+uxNAxa2MfsFzgw8C1GN3SwXfW4ABMO21JsEhGtxFMSpa11+LI1bMfAJf8wgroGMS1jKmVqKdM7+qyLPKJmcQVWxkBH34ahnHGaIbAnUP0TGvjcHWS0Yco5+lNI2
  template:
    metadata:
      annotations:
        sealedsecrets.bitnami.com/cluster-wide: "true"
      creationTimestamp: null
      labels:
        argocd.argoproj.io/secret-type: repository
      name: github-argocd-repo
      namespace: argocd
EOF
    EOT
  }
}

resource "helm_release" "argocd" {
  name  = "argocd"
  repository       = "https://argoproj.github.io/argo-helm"
  chart            = "argo-cd"
  namespace        = "argocd"
  version          = "7.3.8"
}

resource "helm_release" "argocd-apps" {
  depends_on = [helm_release.argocd]
  chart      = "argocd-apps"
  name       = "argocd-apps"
  namespace  = "argocd"
  repository = "https://argoproj.github.io/argo-helm"
  values = [
      file("${path.module}/app-of-apps.yaml")
    ]
}
