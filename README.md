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
