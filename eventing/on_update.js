// Couchbase Eventing Function Template
// Use this template to create dynamic event-driven logic for your application.
// Update BUCKET_NAME, SCOPE_NAME, and COLLECTION_NAME as needed for your deployment.

// Example: Dynamic Alert on Document Update
function OnUpdate(doc, meta) {
    // Trigger logic for documents with a specific prefix or pattern
    if (meta.id.startsWith("EVENT_PREFIX::")) {
        var eventDoc = {
            type: "event_type_here",           // e.g., "combat_alert"
            event_id: meta.id,
            // Add relevant fields from the source document
            field1: doc.field1,                // e.g., doc.system_id
            field2: doc.field2,                // e.g., doc.participants
            status: doc.status,
            timestamp: new Date().toISOString(),
            message: "Describe the event here."
        };
        // Write to the target collection (update as needed)
        // e.g., alerts[meta.id] = eventDoc;
        TARGET_COLLECTION[meta.id] = eventDoc;
    }
}

// --- Deployment Notes ---
// - Replace EVENT_PREFIX, event_type_here, and field names with your actual use case.
// - Set up a binding for TARGET_COLLECTION in the Eventing Function's settings:
//     - Type: "collection"
//     - Alias: TARGET_COLLECTION
//     - Bucket/Scope/Collection: your target location for event documents
// - See: https://docs.couchbase.com/server/current/eventing/eventing-language-constructs.html