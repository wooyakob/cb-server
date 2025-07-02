# Vector Search Example (Couchbase Python SDK)
# https://docs.couchbase.com/server/current/fts/fts-vector-search.html
# Run vector search queries from the CLI using the Couchbase Python SDK.

import os
from dotenv import load_dotenv
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, SearchOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import couchbase.search as search
from couchbase.vector_search import VectorQuery, VectorSearch

# If using embeddings, import your embedding model here
# Example: from langchain_huggingface import HuggingFaceEmbeddings

# --- Environment Setup ---
load_dotenv()

# --- Embedding Model Setup (replace with your preferred model) ---
# Example using HuggingFaceEmbeddings:
# from langchain_huggingface import HuggingFaceEmbeddings
# embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# question = "your search prompt here"
# vector = embeddings_model.embed_query(question)

# --- Couchbase Connection ---
pa = PasswordAuthenticator(
    os.getenv("COUCHBASE_USERNAME"),
    os.getenv("COUCHBASE_PASSWORD")
)
cluster = Cluster(
    os.getenv("COUCHBASE_ENDPOINT"),
    ClusterOptions(pa)
)

# --- Replace with your actual bucket, scope, and index names ---
BUCKET_NAME = "BUCKET_NAME"
SCOPE_NAME = "SCOPE_NAME"
COLLECTION_NAME = "COLLECTION_NAME"
SEARCH_INDEX_NAME = "SEARCH_INDEX_NAME"

bucket = cluster.bucket(BUCKET_NAME)
scope = bucket.scope(SCOPE_NAME)

# --- Vector Search Query ---
# Replace 'vector' with your actual embedding vector
vector = [0.0] * 384  # <-- Placeholder: replace with your generated vector

try:
    search_req = search.SearchRequest.create(search.MatchNoneQuery()).with_vector_search(
        VectorSearch.from_vector_query(VectorQuery('embedding', vector, num_candidates=5))
    )
    
    result = scope.search(
        SEARCH_INDEX_NAME,
        search_req,
        SearchOptions(limit=10, fields=["name", "description", "embedding"])
    )
    
    for row in result.rows():
        print("Found row: {}".format(row))
    
    print("Reported total rows: {}".format(result.metadata().metrics().total_rows()))
except CouchbaseException as ex:
    import traceback
    traceback.print_exc()