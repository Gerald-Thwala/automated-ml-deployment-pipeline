provider "aws" {
  region = var.region
}

# S3 bucket for model storage
resource "aws_s3_bucket" "ml_model_bucket" {
  bucket = var.bucket_name
  force_destroy = true
}

# IAM Role for SageMaker
resource "aws_iam_role" "sagemaker_execution_role" {
  name = "sagemaker_execution_role"
  assume_role_policy = data.aws_iam_policy_document.sagemaker_assume_role_policy.json
}

data "aws_iam_policy_document" "sagemaker_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["sagemaker.amazonaws.com"]
    }
  }
}

# ECR Repository
resource "aws_ecr_repository" "ml_repo" {
  name = var.ecr_repo_name
}

# Output values
output "s3_bucket" {
  value = aws_s3_bucket.ml_model_bucket.bucket
}

output "ecr_repo_url" {
  value = aws_ecr_repository.ml_repo.repository_url
}
