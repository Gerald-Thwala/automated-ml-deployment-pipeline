variable "region" {
  default = "us-east-1"
}

variable "bucket_name" {
  description = "S3 bucket name for ML models"
  type        = string
}

variable "ecr_repo_name" {
  description = "ECR repository name"
  type        = string
}
