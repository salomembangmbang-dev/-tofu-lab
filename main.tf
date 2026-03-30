terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

# Build dell'immagine della TUA app
resource "docker_image" "api" {
  name = "uvicorn-api:latest"

  build {
    context = "."
  }
}


#Aggiungo volume persistente
resource "docker_volume" "data" {
  name = "uvicorn-data"
}

# Container della TUA app
resource "docker_container" "api" {
  name  = "uvicorn-api"
  image = docker_image.api.image_id

  ports {
    internal = 8000
    external = 8000
  }

volumes {
    volume_name    = docker_volume.data.name
    container_path = "/data"
  }
}