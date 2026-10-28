from langchain_core.documents import Document

def create_document(train):
    documents = []
    for item in train:
        temp = Document(
            page_content=item['text'],
            metadata={
                'docid': item['docid'],
                'title': item['title']
            }
        )
        documents.append(temp)
    return documents