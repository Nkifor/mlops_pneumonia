# Xray pneumonia detector to differentiate ill and healthy patient

![Screenshot](xraychests.png)


## Main technologies used:

![Tensorflow](https://img.shields.io/badge/tensorflow-%23FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)
![Github Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![AWS ECR](https://img.shields.io/badge/aws-ecr-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS EC2](https://img.shields.io/badge/aws-ec2-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-%23FF6F00.svg?style=for-the-badge&logo=DVC&logoColor=white)


## Description and shortened context of the training data

The dataset is organized in one main folder : xraychest and folder for separate imaginery classes : (Pneumonia 2 types/Normal).

- 1341 records - normal
- 2530 records pneumonia bacteria
- 1345 records pneumonia virus

As mentioned in source of train dataset:
Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.

For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.


## Stages of the project

1. Planning desired outcome
2. Configuration of environment setup
3. Preparation of notebook every step and refactoring to modular form
4. Initialization DVC repository
5. Prediction expreriments
6. Deployment of model


## Iterative workflows for particular parts of the project

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml




## Context source:
http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5

## Dataset source:
1. https://data.mendeley.com/datasets/rscbjbr9sj/2 - main source of data
2. https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia?datasetId=17810 -  source of this train dataset (in original source there is also test and validating dataset)



# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment

## With acces specified below

 - EC2 access : It is virtual machine
 - ECR: Elastic Container registry to save your docker image in aws


## Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

## Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
 - Save the URI: 325653208527.dkr.ecr.eu-central-1.amazonaws.com/pneumonia
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:

#Optional

sudo apt-get update -y

sudo apt-get upgrade

## Required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = pneumonia