from CNN_pneumonia_xray_detector.config.configuration import ConfigurationManager
from CNN_pneumonia_xray_detector.components.evaluation import Evaluation
from CNN_pneumonia_xray_detector import logger



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> Stage | {STAGE_NAME} | Started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage | {STAGE_NAME} | Finished <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            