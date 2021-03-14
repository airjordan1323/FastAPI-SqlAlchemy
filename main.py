import uvicorn
from fastapi import FastAPI

# from microblog.models import Post

app = FastAPI()


# @app.get('/')
# async def myV(req=None):
#     return {"msg": "ddd"}
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
