import os 
import pandas as pd 
from io import StringIO
from dotenv import load_dotenv 

if not os.getenv("OPENAI_API_KEY"):

    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it up in a .env file.")



def save_chat_to_csv(chat_history):
    df = pd.DataFrame(chat_history)
    csv = StringIO()
    df.to_csv(csv, index=False)
    csv.seek(0)
    return csv.getvalue()