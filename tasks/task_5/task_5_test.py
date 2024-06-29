import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient


# Import Task libraries
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

class ChromaCollectionCreator:

    def __init__(self, processor, embed_model):
        """
        Initializes the ChromaCollectionCreator with a DocumentProcessor instance and embeddings configuration.
        :param processor: An instance of DocumentProcessor that has processed documents.
        :param embeddings_config: An embedding client for embedding documents.
        """
        self.processor = processor  # This will hold the DocumentProcessor from Task 3
        self.embed_model = embed_model  # This will hold the EmbeddingClient from Task 4
        self.db = None  # This will hold the Chroma collection    
    def create_chroma_collection(self):
        """
        Task: Create a Chroma collection from the documents processed by the DocumentProcessor instance.        Steps:
        1. Check if any documents have been processed by the DocumentProcessor instance. If not, display an error message using streamlit's error widget.        2. Split the processed documents into text chunks suitable for embedding and indexing. Use the CharacterTextSplitter from Langchain to achieve this. You'll need to define a separator, chunk size, and chunk overlap.
        https://python.langchain.com/docs/modules/data_connection/document_transformers/        3. Create a Chroma collection in memory with the text chunks obtained from step 2 and the embeddings model initialized in the class. Use the Chroma.from_documents method for this purpose.
        https://python.langchain.com/docs/integrations/vectorstores/chroma#use-openai-embeddings
        https://docs.trychroma.com/getting-started
        """        # Step 1: Check for processed documents
        if len(self.processor.pages) == 0:
            st.error("No documents found!")
            return        # Step 2: Split documents into text chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",  # Define a suitable separator
            chunk_size=1000,  # Define the chunk size
            chunk_overlap=200  # Define the chunk overlap
        )        
        
        chunks = []

        for doc in self.processor.pages:
            # Ensure the Document object has the correct attribute/method for text content
            if hasattr(doc, 'page_content'):  # Adjust 'content' to the correct attribute name if necessary
                doc_text = doc
                chunks.extend(text_splitter.split_documents([doc_text]))
            else:
                st.error("Document object does not have the expected 'content' attribute.")
                return 
             
                   
        if chunks:
            st.success(f"Successfully split pages into {len(chunks)} documents!")
        else:
            st.error("Failed to split documents into chunks!")
            return True     
        
        # Step 3: Create the Chroma Collection
        
        try:
            self.db = Chroma.from_documents(
                documents=chunks,
                embedding=self.embed_model
            )
            st.success("Successfully created Chroma Collection!")
        except Exception as e:
            st.error(f"Failed to create Chroma Collection: {str(e)}")    
            
    def query_chroma_collection(self, query) -> Document:
        """
        Queries the created Chroma collection for documents similar to the query.
        :param query: The query string to search for in the Chroma collection.        Returns the first matching document from the collection with similarity score.
        """
        if self.db:
            docs = self.db.similarity_search(query)
            if docs:
                return docs[0]
            else:
                st.error("No matching documents found!")
        else:
            st.error("Chroma Collection has not been created!")
    
if __name__ == "__main__":
    processor = DocumentProcessor()  # Initialize from Task 3
    processor.ingest_documents()    
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "gemini-quizify-426909",
        "location": "us-central1"
    }    
    
    embed_client = EmbeddingClient(**embed_config)  # Initialize from Task 4    
    chroma_creator = ChromaCollectionCreator(processor, embed_client)    
    with st.form("Load Data to Chroma"):
        st.write("Select PDFs for Ingestion, then click Submit")       
        submitted = st.form_submit_button("Submit")

    if submitted:
        chroma_creator.create_chroma_collection()