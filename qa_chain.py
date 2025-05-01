from langchain.chains import RetrievalQA 
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
load_dotenv()

def get_qa_chain(retriever):
    llm = ChatOpenAI(temperature=0)
    chain = RetrievalQA.from_chain_type(llm = llm , retriever = retriever, chain_type="stuff")
    return chain