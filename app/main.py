from typing import List, Optional

from fastapi import FastAPI, Request, Path, HTTPException, status

from app.logger import logger

app = FastAPI(title="File storage")


@app.on_event("startup")
async def storage_setup_at_startup():
    app.state.fibonacci_storage = {}
    logger.info('Fibonacci storage inited')


def build_fibonacci_array(start_from):
    pass


@app.get('/fibonacci', response_model=List[int])
def fibonacci_api(request: Request, start_from: int = Path(..., ge=0), to: int = Path(..., ge=0)):
    if start_from > to:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='"to" parameter must be greater than "start_from"'
        )
    fibonacci_storage = request.app.state.fibonacci_storage

    return []


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
