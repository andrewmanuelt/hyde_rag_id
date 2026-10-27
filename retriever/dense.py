import chromadb

from langchain_core.documents import Document
from langchain_chroma import Chroma

class DenseRetriever():
    def __init__(self, collection, persistent_directory):
        self.collection = collection
        self.persistent_directory = persistent_directory
        
    def create_or_get_collection(self):
        pass 
    
    def client(self):
        return Chroma(
            collection_name=self.collection,
            persist_directory=self.persistent_directory
        ) 
    
    def get_collection(self):
        pass