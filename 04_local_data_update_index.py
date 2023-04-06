import os
import logging
from pathlib import Path

from llama_index import (
    GPTSimpleVectorIndex, 
    GPTSimpleKeywordTableIndex, 
    SimpleDirectoryReader
)
from llama_index.indices.composability import ComposableGraph

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("BUILD_INDEX")

openai_api_key = os.environ.get('OPENAI_API_KEY')


# Load Documents
cv_root_directory = Path()/'data'

for directory_index in range(1,4):
    document = SimpleDirectoryReader(cv_root_directory/f'cv{directory_index}').load_data()
    index = GPTSimpleVectorIndex.from_documents(document)

    index_file = Path()/'data'/f'cv_{directory_index}_index.json'
    # save index to disk
    index.save_to_disk(index_file)

# Select one index to prove need for composability
# load index from disk
index = GPTSimpleVectorIndex.load_from_disk(cv_root_directory/'cv_1_index.json')
# Query index
spock_address = index.query("Where does Spock Sarek Live ?")
logger.info(spock_address)
uhura_address = index.query("Where does Uhura Live ?")
logger.info(uhura_address)

# Compose indices for query
# Generate indices from files
index_cv_1 = GPTSimpleVectorIndex.load_from_disk(cv_root_directory/'cv_1_index.json')
index_cv_2 = GPTSimpleVectorIndex.load_from_disk(cv_root_directory/'cv_2_index.json')
index_cv_3 = GPTSimpleVectorIndex.load_from_disk(cv_root_directory/'cv_3_index.json')

# Write up summaries
cv_1_summary="Curriculum Vitae of Nyota Uhura"
cv_2_summary="Curriculum Vitae of Spock Sarek"
cv_3_summary="Curriculum Vitae of James T. Kirk"

# set query config
query_configs = [
    {
        "index_struct_type": "simple_dict",
        "query_mode": "default",
        "query_kwargs": {
            "similarity_top_k": 1
        }
    },
    {
        "index_struct_type": "keyword_table",
        "query_mode": "simple",
        "query_kwargs": {}
    },
]

index_all_cvs = ComposableGraph.from_indices(
    GPTSimpleKeywordTableIndex,
    [index_cv_1, index_cv_2, index_cv_3], 
    index_summaries=[cv_1_summary, cv_2_summary, cv_3_summary],
    max_keywords_per_chunk=50
)

# Query again across indices
spock_address = index_all_cvs.query("Where does Spock Sarek Live ?")
uhura_actress = index_all_cvs.query("Who played Nyota Uhura ?")
kirk_players = index_all_cvs.query("Where has James Kirk been portrayed ?")
logger.info(spock_address)
logger.info(uhura_actress)
logger.info(kirk_players)

