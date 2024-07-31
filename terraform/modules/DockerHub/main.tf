# No longer needed, but kept for reference. I used SealedSecret instead, which is more secure.

resource "kubernetes_secret" "docker-registry" {
  metadata {
    name = "regsecret"
  }

  data = {
    ".dockerconfigjson" = "${data.template_file.docker_config_script.rendered}"
  }

  type = "kubernetes.io/dockerconfigjson"
}


data "template_file" "docker_config_script" {
  template = "${file("${path.module}/config.json")}"
  vars = {
    docker-username           = "${var.docker-username}"
    docker-password           = "${var.docker-password}"
    docker-server             = "${var.docker-server}"
    docker-email              = "${var.docker-email}"
    auth                      = base64encode("${var.docker-username}:${var.docker-password}")
  }
}
