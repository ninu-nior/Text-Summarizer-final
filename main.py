from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeling

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataIngestionTrainingPipeling()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e