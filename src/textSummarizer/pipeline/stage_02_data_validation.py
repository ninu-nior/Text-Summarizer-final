#Now component creation is done, now we have to create a pipeline
#first we will handle the try except block, we will initialize configuration manager,
#we will take the data ingestion configuration and store it 
#then we will call the data ingestion components and it will take those data ingestion configuration,
# then we will execute those two methods, download the data and extract the zip file
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.entity import DataValidationConfig

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_validation_config=config.get_data_validation_config()
            data_validation=DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise e