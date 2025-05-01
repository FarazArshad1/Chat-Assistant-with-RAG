from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import os 

def ingest_documents(files):
    all_chunks = []
    for file in files:
        temp_path = f"temp_{file.name}"
        with open(temp_path, "wb") as f:
            f.write(file.read())
        loader = PyPDFLoader(temp_path)
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)
        all_chunks.extend(chunks)
        os.remove(temp_path)

    vectorstore = FAISS.from_documents(all_chunks, OpenAIEmbeddings())
    return vectorstore.as_retriever()

