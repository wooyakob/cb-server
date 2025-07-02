-- Couchbase Analytics Service Template
-- Replace BUCKET_NAME, SCOPE_NAME, and COLLECTION_NAME with your actual names.

-- 1. Create an Analytics Dataset
-- This links your operational data to the Analytics Service.
CREATE DATASET dataset_name ON `BUCKET_NAME`.`SCOPE_NAME`.`COLLECTION_NAME`;

-- 2. (Optional) Connect the Analytics link if not already connected
-- (Uncomment if needed)
-- CONNECT LINK Local;

-- 3. Example Query: Top N Documents by a Numeric Field
SELECT field1, field2, numeric_field
FROM dataset_name
ORDER BY numeric_field DESC
LIMIT 5;

-- 4. Example Query: Aggregate Calculation
SELECT 
  field1,
  field2,
  (numeric_field1 + numeric_field2 + numeric_field3) AS total_value
FROM dataset_name
ORDER BY total_value DESC
LIMIT 1;

-- --- Usage Notes ---
-- - Replace dataset_name and field names with your actual dataset and document fields.
-- - Run these statements in the Couchbase Analytics Workbench or REST API.
-- - See: https://docs.couchbase.com/server/current/analytics/introduction.html