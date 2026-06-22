Document Q&A Bot using RAG, LangChain, ChromaDB, and Gemini

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Question Answering system that allows users to ask questions about a collection of PDF documents.

The application retrieves relevant document sections using semantic search and generates accurate answers using Google's Gemini LLM. Source citations are also displayed to improve transparency and reliability.


Features

* PDF document ingestion
* Automatic text chunking
* Semantic embeddings using Sentence Transformers
* Vector storage using ChromaDB
* Retrieval-Augmented Generation (RAG)
* Gemini-powered answer generation
* Source citation support
* Interactive Streamlit web interface

Tech Stack

* Python
* LangChain
* ChromaDB
* Google Gemini API
* Hugging Face Sentence Transformers
* Streamlit

roject Architecture

text
PDF Documents
      │
      ▼
PyPDFLoader
      │
      ▼
Text Chunking
      │
      ▼
MiniLM Embeddings
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Retrieved Context
      │
      ▼
Gemini LLM
      │
      ▼
Answer + Citations


Project Structure

text
basic-rag-bot/
│
├── .env
├── app.py
├── requirements.txt
│
├── data/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
│
├── vector_db/
│
└── src/
    └── ingest.py


Installation

Clone Repository

```bash
git clone https://github.com/yourusername/basic-rag-bot.git
cd basic-rag-bot
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Configure Gemini API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Prepare Documents

Place PDF files inside the `data` folder:

```text
data/
├── AI.pdf
├── Blockchain.pdf
├── Cybersecurity.pdf
├── IoT.pdf
```

---

Build Vector Database

Run:

```bash
python src/ingest.py
```

Expected output:

```text
Loaded 50 pages
Created 120 chunks
Vector database created successfully
```

---

Launch Application

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

Sample Questions

* What is TCP?
* Explain IPv6 addressing.
* What are the characteristics of IoT?
* What is blockchain technology?
* Explain cybersecurity threats.

---

How It Works

1. PDF documents are loaded using PyPDFLoader.
2. Documents are split into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User queries are converted into embeddings.
6. Relevant chunks are retrieved through similarity search.
7. Retrieved context is sent to Gemini.
8. Gemini generates an answer grounded in the retrieved documents.
9. Source citations are displayed.

---

Future Enhancements

* Multi-format document support (DOCX, TXT, PPT)
* Chat history and conversational memory
* Hybrid search (keyword + semantic)
* User authentication
* Cloud deployment
* Support for multiple LLM providers

---

## Author

Varun

AI Developer | Machine Learning Enthusiast | Data Science Learner
