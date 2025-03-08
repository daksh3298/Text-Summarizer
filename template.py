import os
from pathlib import Path
# for logging runtime information
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
 
 # Defning project name
project_name = 'text_summarizer'

list_of_files = [
                 '.github/workflows/.gitkeep',
                 f'src/{project_name}/__init__.py',
                 f'src/{project_name}/components/__init__.py',
                 f'src/{project_name}/utils/__init__.py',
                 f'src/{project_name}/utils/common.py',
                 f'src/{project_name}/logging/__init__.py',
                 f'src/{project_name}/config/__init__.py',
                 f'src/{project_name}/config/configuration.py',
                 f'src/{project_name}/pipeline/__init__.py',
                 f'src/{project_name}/entity/__init__.py',
                 f'src/{project_name}/constants/__init__.py',
                 'config/config.yaml',
                 'params.yaml',
                 'app.py',
                 'main.py',
                 'Dockerfile',
                 'reqirements.txt',
                 'setup.py'
                 'research/trials.ipynb'
                 
               ]

for file in list_of_files:
    file_path = Path(file)
    filedir,file = os.path.split(file_path)  

    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info('Directory created')

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            pass
            logging.info(f'{file} created')  # log the file creation

    else:
        logging.info(f'{file} already exists')  # log the file creation
        

