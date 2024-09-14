from dataclasses import dataclass
from pathlib import Path

#now define a decorator
#this is not a python actual class, it is a data class, you can mention your variables here
#this eentire thing is an entity, it is the return type of a function
#whenever we create data ingestion configuration, at the time, dataingestionclass will return these variables
#we can take these variables and use it, when we call root_dir, it will automatically return that path mentioned in yaml
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL:str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list