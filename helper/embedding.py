from langchain_huggingface import HuggingFaceEmbeddings

def load_embedding():
    return HuggingFaceEmbeddings(
        model_name='intfloat/multilingual-e5-base',
        encode_kwargs={'normalize_embeddings': True}
    )