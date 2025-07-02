# cb-server
**Enterprise Edition v. 7.6.6**  
_Single node cluster_

---
## Services Enabled
- **Index**
- **Query**
- **Search**
- **Analytics**
- **Eventing**
---

## Cluster Service Overview
See [`cluster/configuration.md`](cluster/configuration.md) for a full template and details.

| Service    | Description                                                                                  |
|------------|----------------------------------------------------------------------------------------------|
| **Data**   | Primary storage for documents. Used for fast CRUD operations.                                |
| **Query**  | Enables N1QL queries for advanced filtering and joins.                                       |
| **Index**  | Supports secondary indexes to speed up queries.                                              |
| **Search** | Full-text and Vector search capabilities for flexible querying.                              |
| **Analytics** | Supports complex aggregations and analytical workloads.                                   |
| **Eventing**  | Enables server-side logic and triggers on data changes.                                   |
| **Backup**    | Handles scheduled and on-demand backups of data.                                          |

---
## Usage
This repository provides Couchbase cluster configuration and index management scripts.
- **Index Builder Template:**  
  See [`indexes/build_indexes.py`](indexes/build_indexes.py) for a template to create indexes for your buckets, scopes, and collections.
- **Cluster Configuration:**  
  See [`cluster/configuration.md`](cluster/configuration.md) for a service template and allocation notes.