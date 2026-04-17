terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3  = "http://127.0.0.1:4566"
    sts = "http://127.0.0.1:4566"
  }
}

# Configuração específica para forçar o S3 a não inventar URLs malucas
resource "aws_s3_bucket" "meu_bucket" {
  bucket = "meu-bucket-de-estaticos"
  
  # Forçar o Terraform a tratar o bucket como um caminho, não um subdomínio
  force_destroy = true
}

# Se o erro persistir, adicione este bloco para garantir o controle total:
resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.meu_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}