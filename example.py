import os
import time
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain_together import Together
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

# Initialize LLM
llm = Together(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    temperature=0.5,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

# Load and split obstetrics-related PDF
loader = PyPDFLoader("gynecologyQA.pdf")
pages = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(pages)

# Create embeddings and vector DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("obstetrics_vector_db")

retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

qa_tool = Tool(
    name="ObstetricsQA",
    func=qa_chain.run,
    description="Answers obstetrics-related questions based on trusted documents."
)

# Tool 1: Obstetric Symptom Checker
def obstetrics_symptom_checker(symptoms: str) -> str:
    symptoms = symptoms.lower()
    if "bleeding" in symptoms:
        return "May indicate threatened miscarriage, placenta previa, or abruptio placentae."
    elif "severe vomiting" in symptoms:
        return "Could be Hyperemesis Gravidarum. Consult a healthcare provider."
    elif "abdominal pain" in symptoms:
        return "Possibly Braxton Hicks contractions or preterm labor if persistent."
    elif "high blood pressure" in symptoms:
        return "Might be a sign of preeclampsia. Monitor closely and consult OB-GYN."
    else:
        return "Symptoms unclear. Please consult an obstetrician for accurate assessment."

symptom_tool = Tool(
    name="ObstetricSymptomChecker",
    func=obstetrics_symptom_checker,
    description="Analyzes symptoms and suggests potential obstetric conditions."
)

# Tool 2: Condition Insight
def obstetrics_cure_insights(condition: str) -> str:
    condition = condition.lower()
    cures = {
        "preeclampsia": "Blood pressure monitoring, magnesium sulfate, early delivery if necessary.",
        "gestational diabetes": "Diet control, exercise, insulin if required.",
        "preterm labor": "Bed rest, tocolytics, corticosteroids for fetal lung maturity.",
        "hyperemesis gravidarum": "IV fluids, antiemetics, hospitalization if severe.",
        "placenta previa": "Pelvic rest, C-section if persists near term."
    }
    for cond, advice in cures.items():
        if cond in condition:
            return f"Management for {cond.capitalize()}: {advice}"
    return "Please consult an obstetrician for personalized care."

cure_tool = Tool(
    name="ObstetricCureInsight",
    func=obstetrics_cure_insights,
    description="Provides management guidance for common obstetric conditions."
)

# Tool 3: Antenatal Care Tips
def antenatal_tips(_: str) -> str:
    return (
        "Antenatal care includes regular checkups, ultrasounds, supplements (iron, folic acid), "
        "monitoring blood pressure, and education on nutrition, hygiene, and labor signs."
    )

antenatal_tool = Tool(
    name="AntenatalCareTips",
    func=antenatal_tips,
    description="Provides essential guidelines and practices during pregnancy."
)

# Memory for conversation
memory = ConversationBufferMemory(memory_key="chat_history")

# Initialize the agent
agent = initialize_agent(
    tools=[symptom_tool, cure_tool, antenatal_tool, qa_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Retry mechanism for user interaction
def ask_obstetric_ai(user_input: str, max_retries=3) -> str:
    retries = 0
    wait_time = 10
    while retries <= max_retries:
        try:
            print("User:", user_input)
            response = agent.run(user_input)
            print("ObstetricAI:", response)
            time.sleep(12)  # delay to respect rate limits
            return response
        except ValueError as e:
            error_msg = str(e)
            if "model_rate_limit" in error_msg:
                print(f"Rate limit hit. Retrying after {wait_time} seconds...")
                time.sleep(wait_time)
                retries += 1
                wait_time *= 2
            else:
                raise
    return "Sorry, the service is busy now. Please try again later."

# Run an example
if __name__ == "__main__":
    ask_obstetric_ai("How is high blood pressure diagnosed and managed?")
