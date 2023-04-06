import os
import logging
from pathlib import Path

from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt, download_loader

# Initialise Logger & environment
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("WIKI-ILIAD")

openai_api_key = os.environ.get('OPENAI_API_KEY')

# Initialise web page loader
SimpleWebPageReader = download_loader("SimpleWebPageReader")
loader = SimpleWebPageReader()

# Tokenize webpage
documents = loader.load_data(urls=['https://arstechnica.com/gadgets/2023/04/9-best-accessories-for-macbook-pro-and-mac-mini/'])
index = GPTSimpleVectorIndex.from_documents(documents)

# Create Prompt & Query String
QA_PROMPT_TMPL = (
    "Hello, I have some context information for you:\n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Based on this context, could you please help me understand the answer to this question: {query_str}?\n"
)
QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

query_str = "What are some Useful accessory upgrades for your MacBook Pro or Mac mini"

# Get response and print answer
response = index.query(query_str, text_qa_template=QA_PROMPT)
logger.info(response)
