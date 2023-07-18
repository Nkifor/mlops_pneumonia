from CNN_Cat_health_classifier.config.configuration import ConfigurationManager
from CNN_Cat_health_classifier.components.prepare_base_model import PrepareBaseModel
from CNN_Cat_health_classifier import logger



STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> Stage | {STAGE_NAME} | Started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage | {STAGE_NAME} | Finished <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f">>>>> Stage | {STAGE_NAME} | Failed")
        raise e
