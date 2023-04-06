import os
import logging
from pathlib import Path

from llama_index import GPTSimpleVectorIndex

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("QUICK-TEST-2")

openai_api_key = os.environ.get('OPENAI_API_KEY')


index_file = Path()/'data'/'index.json'
# load from disk
index = GPTSimpleVectorIndex.load_from_disk(index_file)

name = index.query("What is the candidate's name?")
address = index.query("Where is the candidate's address?")

logger.info(name)
logger.info(address)


