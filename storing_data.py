import os
from langchain.vectorstores import FAISS  # Import FAISS instead of Chroma
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils import download_embeddings

# Download embeddings
embedding = download_embeddings()

# Load PDF documents from the "data" directory
loader = DirectoryLoader("data", glob="*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

# Split documents into chunks
doc_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=20)
docs = doc_splitter.split_documents(documents)

# Create FAISS vector store
vectorstore = FAISS.from_documents(
    documents=docs,  # Use the split documents
    embedding=embedding  # Use the downloaded embeddings
)

# Save the FAISS index locally
persist_directory = 'faiss_index'
vectorstore.save_local(persist_directory)

print(f"FAISS index saved to {persist_directory}")