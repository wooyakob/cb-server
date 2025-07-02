# Couchbase Query Script Template
# Generic script for querying documents from a Couchbase collection using the Python SDK.
# Update BUCKET_NAME, SCOPE_NAME, and COLLECTION_NAME as needed.

import os
from datetime import timedelta
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from dotenv import load_dotenv

load_dotenv()

# --- Credentials ---
username = os.getenv("COUCHBASE_USERNAME")
password = os.getenv("COUCHBASE_PASSWORD")
couchbase_url = os.getenv("COUCHBASE_ENDPOINT")

# --- Target (update these placeholders) ---
BUCKET_NAME = "BUCKET_NAME"
SCOPE_NAME = "SCOPE_NAME"
COLLECTION_NAME = "COLLECTION_NAME"

auth = PasswordAuthenticator(username, password)
cluster = Cluster(couchbase_url, ClusterOptions(auth))
cluster.wait_until_ready(timedelta(seconds=5))

bucket = cluster.bucket(BUCKET_NAME)
scope = bucket.scope(SCOPE_NAME)
collection = scope.collection(COLLECTION_NAME)

# --- Query Example (update as needed) ---
query_str = f"SELECT * FROM `{BUCKET_NAME}`.`{SCOPE_NAME}`.`{COLLECTION_NAME}` LIMIT 10;"
result = cluster.query(query_str)

print(f"Results from `{BUCKET_NAME}`.`{SCOPE_NAME}`.`{COLLECTION_NAME}`:")
for row in result:
    doc = row.get(COLLECTION_NAME, row)
    print(doc)