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

## 🧱 Project Structure

