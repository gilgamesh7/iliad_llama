
import os

from llama_index import StringIterableReader, GPTTreeIndex


openai_api_key = os.environ.get('OPENAI_API_KEY')

input_question = "How tall is Tom Hiddleston"
input_question = "Who is taller Tom Hiddleston or Chris Hemsworth"
input_question_list = []
input_question_list.append(input_question)


documents = StringIterableReader().load_data(texts=input_question_list)
index = GPTTreeIndex.from_documents(documents)

response = index.query("Is this text comparing two or more things? Give a True or False answer")

print(response)

