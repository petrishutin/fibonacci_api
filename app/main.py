from fastapi import FastAPI

app = FastAPI(title="File storage")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
