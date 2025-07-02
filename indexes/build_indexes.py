import os
from dotenv import load_dotenv
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

load_dotenv()

username = os.getenv("COUCHBASE_USERNAME")
password = os.getenv("COUCHBASE_PASSWORD")
couchbase_url = os.getenv("COUCHBASE_ENDPOINT")

cluster = Cluster(
    couchbase_url,
    ClusterOptions(PasswordAuthenticator(username, password))
)

# Replace BUCKET, SCOPE, COLLECTION, and FIELD_NAME
index_queries = [
    "CREATE INDEX idx_collection_field1 ON `BUCKET`.`SCOPE`.`COLLECTION`(FIELD_NAME1);",
    "CREATE INDEX idx_collection_field2 ON `BUCKET`.`SCOPE`.`COLLECTION`(FIELD_NAME2);",
    # Array Index:
    "CREATE INDEX idx_collection_array_field ON `BUCKET`.`SCOPE`.`COLLECTION`(DISTINCT ARRAY item FOR item IN ARRAY_FIELD END);",
]

for query in index_queries:
    try:
        cluster.query(query).execute()
        print(f"Executed: {query}")
    except Exception as e:
        print(f"Error executing: {query}\n{e}")