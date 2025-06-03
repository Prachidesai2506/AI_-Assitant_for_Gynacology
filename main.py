import os
import time
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain_together import Together

# Load environment variables
load_dotenv()

# Initialize LLM
llm = Together(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    temperature=0.5,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

# # Load and split PDF (commented out if vector DB already created)
# loader = PyPDFLoader("gynecologyQA.pdf")
# pages = loader.load()
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# docs = text_splitter.split_documents(pages)
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
# vectorstore = FAISS.from_documents(docs, embeddings)
# vectorstore.save_local("obstetrics_vector_db")

# Load embeddings and vector DB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = FAISS.load_local("obstetrics_vector_db", embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Define QA tool function with safe extraction of 'result'
def qa_tool_func(query: str) -> str:
    try:
        result = qa_chain.invoke({"query": query})
        # Return just the answer text
        return result.get("result", "Sorry, I could not find an answer.")
    except Exception as e:
        return f"Error in QA chain: {str(e)}"

# QA Tool
qa_tool = Tool(
    name="ObstetricsQA",
    func=qa_tool_func,
    description="Answers obstetrics-related questions based on trusted documents."
)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Initialize agent with parsing error handling enabled
agent = initialize_agent(
    tools=[qa_tool],
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True  # <-- This allows retrying parse errors
)

# Retry mechanism with broad exception handling
def ask_obstetric_ai(user_input: str) -> str:
    try:
        print("User:", user_input)
        result = qa_chain.invoke({"query": user_input})
        response = result.get("result", "No answer found.")
        print("ObstetricAI:", response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while fetching the answer."


# Run example
if __name__ == "__main__":
    ask_obstetric_ai("How is high blood pressure diagnosed and managed during pregnancy?")
