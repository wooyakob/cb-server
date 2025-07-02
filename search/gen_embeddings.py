# Embedding Generation Script Template
# Generates embeddings for documents using a HuggingFace model and saves them to a JSON file.
# No specific data schema or fields are required—update as needed for your use case.

import os
import json
from dotenv import load_dotenv
load_dotenv()

# --- Embedding Model Setup ---
# Replace with your preferred embedding model if needed
from langchain_huggingface import HuggingFaceEmbeddings
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# --- Input/Output Paths ---
input_path = os.getenv("INPUT_PATH")      # Path to input JSON file
output_path = os.getenv("OUTPUT_PATH")    # Path to save output JSON with embeddings

with open(input_path, "r", encoding="utf-8") as f:
    items = json.load(f)

updated_items = []

for item in items:
    # Update these field names as needed for your data
    name = item.get("name", "").strip()
    description = item.get("description", "").strip()
    
    if not name:
        print("Skipping item with missing name.")
        continue

    combined_text = f"Name: {name}\nDescription: {description}"
    embedding_vector = embeddings_model.embed_documents([combined_text])[0]
    item["embedding"] = embedding_vector
    updated_items.append(item)
    
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(updated_items, f, indent=4)

print(f"Embeddings generated and saved to: {output_path}")