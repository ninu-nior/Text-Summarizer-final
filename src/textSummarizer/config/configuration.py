#import all the constants
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = Path("config/config.yaml"),
        params_filepath=PARAMS_FILE_PATH
    ):
        #it will read this yaml file and we can access all the variables
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            
        )
        return data_ingestion_config
    #hence we have created our custom datatype of any function using dataclass we call it entity
    #now we can easily call the dataIngestion configuration and access everything
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        create_directories([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
        return data_validation_config