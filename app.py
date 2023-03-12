# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import numpy as np
import json


qdrant_client = QdrantClient(host='localhost', port=6333)

# Create collection
qdrant_client.recreate_collection(
    collection_name='startups', 
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

qdrant_client.upload_collection(
    collection_name='startups',
    vectors=[
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
    ],
    payload=[
        {'name': 'Apple', 'country': 'USA'},
        {'name': 'Google', 'country': 'USA'},
        {'name': 'Yandex', 'country': 'Russia'},
        {'name': 'Samsung', 'country': 'South Korea'},
        {'name': 'Huawei', 'country': 'China'},
        {'name': 'Microsoft', 'country': 'USA'},
        {'name': 'Facebook', 'country': 'USA'},
        {'name': 'Amazon', 'country': 'USA'},
        {'name': 'Alibaba', 'country': 'China'},
        {'name': 'Tencent', 'country': 'China'},
        {'name': 'Baidu', 'country': 'China'},
        {'name': 'Sony', 'country': 'Japan'},
        {'name': 'LG', 'country': 'South Korea'},
        {'name': 'Nokia', 'country': 'Finland'},
        {'name': 'Intel', 'country': 'USA'},
    ],
    batch_size=256
)
