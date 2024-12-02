import google.generativeai as gemini_client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

collection_name = "example_collection"

GEMINI_API_KEY = "YOUR GEMINI API KEY"  # add your key here

client = QdrantClient(url="https://5299250f-c13d-46b8-87af-f93cea7907cb.europe-west3-0.gcp.cloud.qdrant.io:6333")
gemini_client.configure(api_key="")
texts = [
    "Qdrant is a vector database that is compatible with Gemini.",
    "Gemini is a new family of Google PaLM models, released in December 2023.",
]

results = [
    gemini_client.embed_content(
        model="models/embedding-001",
        content=sentence,
        task_type="retrieval_document",
        title="Qdrant x Gemini",
    )
    for sentence in texts
]