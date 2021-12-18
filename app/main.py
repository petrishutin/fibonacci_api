from typing import List, Optional

from fastapi import FastAPI, Request, Query, HTTPException, status

from app.logger import logger
from app.fibonacci_array import build_fibonacci_array

app = FastAPI(title="File storage")


@app.on_event("startup")
async def storage_setup_at_startup():
    app.state.fibonacci_storage = {}
    logger.info('Fibonacci storage inited')


@app.get('/fibonacci', response_model=List[int])
def fibonacci_api(request: Request, start_from: int = Query(..., ge=0), to: int = Query(..., ge=0)):
    if start_from > to:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='"to" parameter must be greater than "start_from"'
        )
    fibonacci_storage = request.app.state.fibonacci_storage
    return build_fibonacci_array(fibonacci_storage, start_from, to)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
