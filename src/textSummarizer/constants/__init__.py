# we want to return config.yaml and params.yaml, to read it, we need a path, so 
#no need to hardcode the path, we can keep in constant

from pathlib import Path

CONFIG_FILE_PATH=Path("config/config.yaml")
PARAMS_FILE_PATH=Path("params.yaml")