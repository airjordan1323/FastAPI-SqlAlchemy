import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from core.db import Sessionlocal
from routes import routes

# from microblog.models import Post

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = Sessionlocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routes)
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
