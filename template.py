import os
from pathlib import Path
import logging#to log all the info
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project_name="textSummarizer"
#.githib is used for whenever we are doing any deployment, actually we just write our CI Cd related eml file
#it will help you do the ci cd deploy,ment,if we want to commit our code in github, so whenever you will do the commit, it will automatically take your code from the github and do the deployment in the cloud
#so thats why the .github is important, whenevr you do the commit, it will automatically take your code from the git and do the deployment in the cloud
#inside that we need anothewr folder called workflows, inside that we will create andther edm file called.gitkeep, because when you commit, empty folders wont be, so we created an emoty file inside it, it is a hidden file
# then we create the constructor file,we need constructor file because this thing actually has installed as my local package, and let's say you want to import something from any folder, because we have created some componenets, so we can directly, do "from textSummarizer import"so to do these kind of import operations, you need to install this as your local package, and to do that, this costructor file is needed
#whenever this constructor file is present, that folder will be considered as your local package
#inside componenets we will create another constructor file because components is another local package
#in the commons file, we keep all the utility code
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
    ]

for filepath in list_of_files:
    #the path rfunction automatically gives a os path based on your os, for windows, it will give a windows path
    
    filepath=Path(filepath)
    #it will split the folder and filename, so that we create the folder first and then the file
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        # now we want to see the logs, so hence the next line
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    #first checking if the file exists or not or checking the size of the file
    if(not os.path.exists(filepath) or (os.path.getsize(filepath))==0):
        #if the file does not exist or the size of the file is 0, then we
        with open(filepath,'w') as f:
            pass
            logging.info(f"creatinf empty file:{filepath}")
    else:
        logging.info(f"file {filename} already exists")
    
    
