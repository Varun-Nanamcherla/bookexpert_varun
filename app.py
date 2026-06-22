import os
import streamlit as st

from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

DB_PATH = "vector_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

st.set_page_config(page_title="Document Q&A Bot")

st.title("📚 Document Q&A Bot")

query = st.text_input("Ask a question")

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a question.")
    else:

        docs = db.similarity_search(
            query,
            k=3
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a document assistant.

Answer ONLY from the provided context.

If the answer is not present, reply:
'I could not find this information in the documents.'

Context:
{context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)

        st.subheader("Sources")

        for doc in docs:
            st.write(
                f"{doc.metadata.get('source')} "
                f"(Page {doc.metadata.get('page')})"
            )