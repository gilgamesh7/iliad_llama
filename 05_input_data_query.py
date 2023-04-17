import os
import logging
from pathlib import Path

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("QUICK-TEST-1")

openai_api_key = os.environ.get('OPENAI_API_KEY')

documents = SimpleDirectoryReader('questions').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
flag = index.query("Give a True or False answer to is this question comparing things?")


logger.info(flag)

