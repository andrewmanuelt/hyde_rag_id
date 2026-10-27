from datasets import load_dataset

print("--- Memuat Korpus (Dokumen Wikipedia Indonesia) ---")
# Memuat koleksi dokumen/pasase untuk bahasa Indonesia ('id')
# Dataset corpus biasanya langsung berbentuk Dataset single split
corpus_ds = load_dataset("miracl/miracl-corpus", "id", split="train", trust_remote_code=True)

print("Jumlah dokumen dalam korpus:", len(corpus_ds))
print("Contoh dokumen:", corpus_ds[0])
# Format isi korpus umumnya berisi: {'docid': '...', 'title': '...', 'text': '...'}


print("\n--- Memuat Queries & Qrels (Pertanyaan & Penilaian Relevansi) ---")
# Memuat bagian query dan qrels (train / dev) untuk bahasa Indonesia ('id')
# Perhatikan bahwa repositori ini mungkin memerlukan autentikasi Hugging Face token jika diminta oleh sistem
queries_ds = load_dataset("miracl/miracl", "id", trust_remote_code=True)

print("Split yang tersedia:", queries_ds.keys())
print("Contoh Query (Train):", queries_ds["train"][0])
# Format query umumnya berisi: {'query_id': '...', 'query': '...', 'positive_passages': [...], 'negative_passages': [...]}

print("=== 1. Memeriksa Queries & Qrels ('miracl/miracl') ===")
# Memuat dataset query MIRACL bahasa Indonesia ('id')
miracl_queries = load_dataset("miracl/miracl", "id", trust_remote_code=True)

# Menampilkan jumlah sampel untuk setiap split yang tersedia
for split_name in miracl_queries.keys():
    num_samples = len(miracl_queries[split_name])
    print(f" - Split '{split_name}': {num_samples:,} query")


print("\n=== 2. Memeriksa Corpus / Dokumen ('miracl/miracl-corpus') ===")
# Memuat korpus dokumen MIRACL bahasa Indonesia ('id')
miracl_corpus = load_dataset("miracl/miracl-corpus", "id", trust_remote_code=True)

# Menampilkan jumlah sampel korpus
for split_name in miracl_corpus.keys():
    num_docs = len(miracl_corpus[split_name])
    print(f" - Split '{split_name}': {num_docs:,} dokumen")