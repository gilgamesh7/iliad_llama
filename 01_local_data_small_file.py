import os
import logging
from pathlib import Path

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("QUICK-TEST-1")

openai_api_key = os.environ.get('OPENAI_API_KEY')

documents = SimpleDirectoryReader('data').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)
name = index.query("What is the candidate's name?")
address = index.query("Where is the candidate's address?")

logger.info(name)
logger.info(address)

index_file = Path()/'data'/'index.json'
# save to disk
index.save_to_disk(index_file)

# load from disk
index = GPTSimpleVectorIndex.load_from_disk(index_file)