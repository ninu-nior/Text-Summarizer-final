import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


# config box, we are returning yaml file as configbox


#first common utility function would be readyaml
# responsibl efor reading any yaml file and returning all the content inside a yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """Reads a yaml file and returns
    Args:
        path_to_yaml(str):path like input
    Raises:
    BoxValueError: if the file is not a valid yaml file
        ValueError:if yaml file is empty
        e:empty file
    Returns:
    ConfigBox: configbox type
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
    
    
#a method to create directories
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    #create a list of directories
    #args:
    # path_to_directories(list): list of path of directories
    # ignore_log(bool,optional):ignore if multiple dirs is to be created,Defaults to False
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")
            
            
            
#this method would return the size of a file
def get_size(path:Path)->str:
    # get size in Kb 
    # args: path(Path): path of the file 
    # returns:file size in kb, str 
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
    
    