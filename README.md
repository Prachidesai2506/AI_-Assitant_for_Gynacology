# 🤖 ObstetricAI - Conversational QA Agent for Obstetrics

ObstetricAI is a conversational AI assistant designed to answer questions related to obstetrics using a custom PDF knowledge base. It uses:
- 🧠 [LangChain](https://www.langchain.com/) for chain and agent orchestration
- 🔍 [FAISS](https://github.com/facebookresearch/faiss) for vector-based retrieval
- 📄 [PDF loader](https://docs.langchain.com/docs/integrations/document_loaders/pdf) to process domain-specific documents
- 🗣️ [Together LLM](https://www.together.ai/) to run `deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free` model for intelligent responses

---

## 🗂️ Features

- Context-aware conversations with memory
- Retrieves information from pre-loaded medical PDF documents
- Handles retries with exponential backoff when hitting rate limits
- Simple CLI-based usage
- Designed for obstetrics-related educational, advisory, or informational use

---


## 🧱 Tech Stack

| Component         | Tool / Library                            |
|------------------|-------------------------------------------|
| LLM              | Together.ai – DeepSeek-LLaMA-70B          |
| Vector DB        | FAISS                                      |
| Embeddings       | sentence-transformers/all-mpnet-base-v2   |
| Framework        | LangChain                                  |
| Memory           | ConversationBufferMemory                   |
| UI               | Streamlit                                  |

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/obstetric-ai.git
cd obstetric-ai


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

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/obstetric-ai.git
cd obstetric-ai

python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

