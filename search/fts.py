# Full Text Search Example (Couchbase Python SDK)
# https://docs.couchbase.com/server/7.1/fts/fts-creating-indexes.html
# Tokenizing and indexing text fields to search for documents using words and phrases, not just exact matches.

import os
from dotenv import load_dotenv
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, SearchOptions
from couchbase.search import QueryStringQuery

# --- Environment Setup ---
load_dotenv()
cluster = Cluster(
    os.getenv("COUCHBASE_ENDPOINT"),
    ClusterOptions(PasswordAuthenticator(
        os.getenv("COUCHBASE_USERNAME"),
        os.getenv("COUCHBASE_PASSWORD")
    ))
)

# --- Full Text Search Template ---
# Replace the following placeholders with your actual bucket, scope, collection, and index names:
#   BUCKET_NAME
#   SCOPE_NAME
#   COLLECTION_NAME
#   SEARCH_INDEX_NAME

# Example search query (update as needed)
query = QueryStringQuery("search terms here")

result = cluster.search_query(
    "SEARCH_INDEX_NAME",  # e.g., "mybucket.myscope.my_search_index"
    query,
    SearchOptions(limit=5)
)

print("[scoped access - bucket:BUCKET_NAME; scope:SCOPE_NAME; collection:COLLECTION_NAME]")
matches = list(result)
print(f"{len(matches)} result(s)\n")

for row in matches:
    doc_id = row.id
    score = row.score
    # Fetch the document from the collection (update names as needed)
    doc = cluster.bucket("BUCKET_NAME").scope("SCOPE_NAME").collection("COLLECTION_NAME").get(doc_id)
    content = doc.content_as[dict]
    print(f"Document ID: {doc_id}")
    print(f"Score: {score}")
    print("Fields:")
    print(f"  name: {content.get('name', '')}")
    print(f"  description: {content.get('description', '')[:120]}...")
    print("-" * 40)