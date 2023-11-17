import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_batch_embeddings(texts):
    responses = openai.Embedding.create(
        input=texts,
        model="text-embedding-ada-002"
    )
    return [response['embedding'] for response in responses['data']]

def get_single_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']
