from openai import OpenAI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import pyodbc 

with open("config.json") as f:
    config = json.load(f)

client = OpenAI(
    api_key=config["OPENAI_API_KEY"]
)

app = FastAPI()
# Allow requests from Angular dev server
origins = [
    "http://localhost:4200",  # Angular dev server
    # Add other origins if needed, e.g. production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],            # allow all HTTP methods
    allow_headers=["*"],            # allow all headers
)


# Request schema
class ChatRequest(BaseModel):
    user_message: str

# Response schema
class ChatResponse(BaseModel):
    reply: str

# You are a SQL expert.
# Convert user question into SQL Server query.

# Rules:
# - Use only given tables
# - Do not delete/update
# - Only SELECT queries
# - Return plain SQL only

# Schema:
# Users(UserId, Name, Email)
# Transactions(Id, UserId, Amount, Date)

def isCallLLM(user_question:str):  
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a SQL expert. Convert user question into SQL Server query. Rules: Use only given tables, Do not delete/update, Only SELECT queries,Where clause always Use UserId, Return plain SQL only. Schema: Users(UserId, Name, Email), Transactions(Id, UserId, Amount, Date)"},
            {"role": "user", "content": user_question}
        ]
    )
    #print(response.choices[0].message.content)
    return response.choices[0].message.content

def is_safe_select(sql_query: str) -> bool:
    sql = sql_query.strip().lower()
    return sql.startswith("select") and not any(
        keyword in sql for keyword in ["insert", "update", "delete", "drop", "alter"]
    )

def execute_sql_query(query,user_id:int) -> list:
    if not is_safe_select(query):
        raise ValueError("Only SELECT queries are allowed.")

    # Database connection parameters
    server = config["DB_SERVER"]
    database = config["DB_DATABASE"]
    username = config["DB_USERNAME"]
    password = config["DB_PASSWORD"]
    
    # Create a connection to the SQL Server database
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    
    # Create a cursor object to execute the query
    cursor = conn.cursor()
    
    # Execute the query
    cursor.execute(query,(user_id,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return results

# print("Executing SQL query...")
# results = execute_sql_query("select * from [dbo].[Users]")
# for row in results:
#     print(row)

def clean_sql_query(llm_output: str) -> str:
    """
    Remove markdown code fences and leading 'sql' from LLM output.
    """
    # Strip whitespace
    query = llm_output.strip()

    # Remove triple backticks and optional 'sql'
    if query.startswith("```sql"):
        query = query[len("```sql"):].strip()
    elif query.startswith("```"):
        query = query[len("```"):].strip()

    # Remove trailing backticks if present
    if query.endswith("```"):
        query = query[:-3].strip()

    return query


def main(user_question:str):
    user_id = 1  # Example user ID for testing
    #user_question = input("Enter your question: ")
    llmquery = isCallLLM(user_question)
    print(llmquery)
    sql_query = clean_sql_query(llmquery).replace("@UserId", "?")
    print("Clean SQL query:")
    print(sql_query)
    print("Executing SQL query...")
    results = execute_sql_query(sql_query, user_id)
    print("Format DataBase Response in natural language...")
    formatted_response = format_for_chatbot(user_question, results)
    print("Chatbot response:")
    print(formatted_response)
    return formatted_response
  

def format_for_chatbot(user_question: str, sql_results: list) -> str:
    """
    Pass SQL results to LLM to format into a natural chatbot response.
    """
    prompt = f"""
    You are a helpful chatbot.
    The user asked: "{user_question}"
    Here are the raw SQL results: {sql_results}

    Please format the answer in a clear, conversational way that is easy for the user to understand.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    print("Received user message:", request.user_message)
    formatted_response = main(request.user_message)
    return ChatResponse(reply=formatted_response)


# if __name__ == "__main__":
#     main()
