
import os

from llama_index import StringIterableReader, GPTTreeIndex
import llama_index

openai_api_key = os.environ.get('OPENAI_API_KEY')

# input_question = "How tall is Tom Hiddleston"
input_question = "Who is taller Tom Hiddleston or Chris Hemsworth"
input_question_list = []
input_question_list.append(input_question)


documents = StringIterableReader().load_data(texts=input_question_list)
index = GPTTreeIndex.from_documents(documents)

response = index.query("Is this text comparing two or more things? Give a True or False answer")

get_comparer_variable_for_true = index.query("return the word True as an answer to this query")
# print(f"I got {get_comparer_variable_for_true} as answer of type {type(get_comparer_variable_for_true)}")
get_comparer_variable_for_false = index.query("return the word False as an answer to this query")


print(f" Response is : [{response}]")
if response == get_comparer_variable_for_true:
    print("Response is True")
else :
    print("Response is not True")

if response == get_comparer_variable_for_false:
    print("Response is False")
else :
    print("Response is not False")

# print(f"Is response instance of type lama_index.response.schema.Response : {isinstance(response, llama_index.response.schema.Response)}")
# my_object = "True"
# my_object_as_Response = llama_index.response.schema.Response(my_object)
# print(f"Typecast {my_object} : {type(my_object_as_Response)}")
# print(f"Is my_object_as_Response instance of type lama_index.response.schema.Response : {isinstance(my_object_as_Response, llama_index.response.schema.Response)}")

# print(f"ID of my_object_as_Response : {my_object_as_Response} - {id(my_object_as_Response)}")
# print(f"ID of response : {response} -  {id(response)}")
# print(f"ID of my_object_as_Response : {my_object_as_Response} - {id(my_object_as_Response)}")
# print(f"Is  my_object_as_Response equal to response ? {my_object_as_Response == response}")
# print(f"Is  my_object_as_Response same as response ? {my_object_as_Response is response}")
