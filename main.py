import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from core.db import database
from routes import routes
from fastapi_users import FastAPIUsers, models
from user.logic import *
from user.schemas import *
# from microblog.models import Post

app = FastAPI()


fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = database()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: User, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token:{token}")

def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")



app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(routes)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
