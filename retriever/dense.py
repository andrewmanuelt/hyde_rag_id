from uuid import uuid4
from tqdm import tqdm
from langchain_chroma import Chroma

from helper.embedding import load_embedding

class DenseRetriever():
    def __init__(self, collection, persistent_directory):
        self.collection = collection
        self.persistent_directory = f'./database/{persistent_directory}'

    def client(self):
        return Chroma(
            embedding_function=load_embedding(),
            collection_name=self.collection,
            persist_directory=self.persistent_directory
        ) 
    
    def create_collection(self, document, num_batch=0):
        if num_batch < 0:
            raise ValueError("num_batch must be zero or a positive integer")

        client = self.client()

        if num_batch == 0:
            batches = [document] if document else []
        else:
            batches = (
                document[start:start + num_batch]
                for start in tqdm(range(0, len(document), num_batch))
            )

        for batch in batches:
            ids = [str(uuid4()) for _ in range(len(batch))]
            client.add_documents(documents=batch, ids=ids)