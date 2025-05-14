# 🚀 Automated ML Model Deployment Pipeline

This project demonstrates a complete end-to-end **MLOps pipeline** for deploying machine learning models using modern DevOps practices and cloud-native tools. It includes model training, Docker containerization, infrastructure automation with Terraform, and CI/CD orchestration using Azure DevOps. The model is served via a REST API deployed to AWS (SageMaker, Lambda, S3, and ECR).

---

## 📌 Features

- ✅ Train and save a machine learning model (e.g., scikit-learn)
- ✅ Containerize the inference API using FastAPI and Docker
- ✅ Deploy to AWS (S3, ECR, SageMaker) via Terraform
- ✅ Automate CI/CD with Azure DevOps
- ✅ Secure and monitor model deployment
- ✅ Modular and production-ready codebase

---

## 🧰 Tech Stack

| Layer              | Tools/Services |
|-------------------|----------------|
| Language           | Python 3.10     |
| Model Serving      | FastAPI         |
| Containerization   | Docker          |
| Infrastructure     | AWS (S3, ECR, SageMaker, Lambda) |
| IaC                | Terraform       |
| CI/CD              | Azure DevOps    |
| Monitoring         | CloudWatch (optional) |
| Version Control    | Git + GitHub    |

---

## 🗂️ Project Structure

automated-ml-deployment-pipeline/
│
├── .azure-pipelines/
│   └── azure-pipelines.yml          # CI/CD pipeline definition
│
├── terraform/
│   ├── main.tf                      # Main infra provisioning
│   ├── variables.tf                 # Input variables
│   ├── outputs.tf                  # Terraform output values
│   └── provider.tf                 # AWS provider setup
│
├── model/
│   ├── train_model.py               # Model training script
│   ├── inference.py                 # Inference logic
│   ├── requirements.txt             # Python dependencies
│   └── model.pkl                    # Trained model (or saved during pipeline)
│
├── docker/
│   ├── Dockerfile                   # Build model serving container
│   └── app/                         
│       ├── main.py                  # Flask/FastAPI entrypoint for inference
│       └── utils.py                 # Pre/post-processing utilities
│
├── scripts/
│   └── upload_to_s3.py              # Script to upload assets to S3
│
├── .gitignore
├── README.md
└── LICENSE
