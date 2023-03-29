from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# That is the file where NeuralSearcher is stored
from main import neural_searcher

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of the neural searcher
neuralsearcher = neural_searcher(collection_name='startups', model_name='distilbert-base-nli-stsb-mean-tokens')

@app.get("/api/search")
def search(text: str):
    # Call the search method
    return {
        'result': neuralsearcher.search(text)
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
