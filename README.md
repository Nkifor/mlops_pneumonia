# Xray pneumonia detector to differentiate ill and healthy patient

![Screenshot](xraychests.PNG)


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
