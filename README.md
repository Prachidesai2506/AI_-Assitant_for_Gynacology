# 🤖 ObstetricAI - Conversational QA Agent for Obstetrics

ObstetricAI is a conversational AI assistant designed to answer questions related to **obstetrics** using a custom PDF knowledge base. Built with powerful LLMs and vector search technology, it provides intelligent and context-aware answers drawn from domain-specific medical documents.

---

## 🧠 Core Technologies

- **[LangChain](https://www.langchain.com/)** for orchestrating chains and managing memory  
- **[FAISS](https://github.com/facebookresearch/faiss)** for fast and efficient vector similarity search  
- **[PDF Loader](https://docs.langchain.com/docs/integrations/document_loaders/pdf)** for extracting text from domain-specific PDFs  
- **[Together.ai](https://www.together.ai/)** running `deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free` for powerful LLM-backed responses  

---

## 🗂️ Features

- 💬 Context-aware conversational AI with memory  
- 📄 Accurate retrieval from uploaded obstetrics-related PDFs  
- 🔁 Built-in retry mechanism using exponential backoff (for rate limits)  
- 💻 CLI-based interaction (Streamlit UI optional)  
- 🧑‍⚕️ Tailored for obstetrics education, awareness, and advisory usage  

---

## 🧱 Tech Stack

| Component         | Tool / Library                            |
|------------------|-------------------------------------------|
| LLM              | Together.ai – DeepSeek-LLaMA-70B          |
| Vector DB        | FAISS                                      |
| Embeddings       | sentence-transformers/all-mpnet-base-v2   |
| Framework        | LangChain                                  |
| Memory           | ConversationBufferMemory                   |
| UI (Optional)    | Streamlit                                  |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/obstetric-ai.git
cd obstetric-ai
2. Create and Activate a Virtual Environment
For macOS/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
For Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
4. Add Your PDF Documents
Place your domain-specific obstetrics PDF files inside the data/ directory. These will be used to build the knowledge base.

5. Configure Environment Variables
Create a .env file in the root directory and add your Together API key:

env
Copy
Edit
TOGETHER_API_KEY=your_together_ai_key
6. Run the CLI Interface
bash
Copy
Edit
python main.py
Or use the Streamlit UI (if included):

bash
Copy
Edit
streamlit run app.py
🧪 Example Questions
What are the early signs of preeclampsia?

How is gestational diabetes managed?

What precautions should be taken during the third trimester?

📁 Project Structure
bash
Copy
Edit
obstetric-ai/
│
├── data/                        # Folder for PDF knowledge base
├── main.py                      # Main script to run the chatbot
├── app.py                       # Optional: Streamlit app interface
├── loader.py                    # PDF loader logic
├── qa_chain.py                  # LangChain-based QA pipeline
├── requirements.txt             # Python dependencies
└── .env                         # API keys and environment settings
