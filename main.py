from CNN_Cat_health_classifier import logger
from CNN_Cat_health_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Cat_health_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNN_Cat_health_classifier.pipeline.stage_03_training import ModelTrainingPipeline
from CNN_Cat_health_classifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage | {STAGE_NAME} | Started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage | {STAGE_NAME} | Finished \n\n ========================================")
except Exception as e:
    logger.exception(f">>>>> Stage | {STAGE_NAME} | Failed")
    raise e



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage | {STAGE_NAME} | Started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} | Finished <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training Stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> Stage | {STAGE_NAME} | Started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage | {STAGE_NAME} | Finished <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f">>>>> Stage | {STAGE_NAME} | Failed")
    raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage | {STAGE_NAME} | Started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(f">>>>> Stage | {STAGE_NAME} | Failed")
        raise e