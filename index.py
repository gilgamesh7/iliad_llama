import os
import logging

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("QUICK-TEST")

openai_api_key = os.environ.get('OPENAI_API_KEY')

documents = SimpleDirectoryReader('data').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)
name = index.query("What is the candidate's name?")
address = index.query("Where is the candidate's address?")

logger.info(name)
logger.info(address)