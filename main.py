from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.controllers import account, auth, transaction
from src.database import database
from src.exceptions import AccountNotFoundError, BusinessError


# Conectar e desconectar o DB
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


# Tags para a documentação
tags_metadata = [
    {"name": "auth", "description": "Operations for authentication."},
    {"name": "account", "description": "Operations to maintain accounts."},
    {"name": "transaction", "description": "Operations to maintain transactions."},
]

# Criar app FastAPI
app = FastAPI(
    title="Transactions API",
    version="1.0.0",
    description="""
Transactions API is the microservice for recording current account transactions. 💸💰

## Account

* **Create accounts**.
* **List accounts**.
* **List account transactions by ID**.

## Transaction

* **Create transactions**.
""",
    openapi_tags=tags_metadata,
    redoc_url=None,
    lifespan=lifespan,
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Routers
app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])


# Tratamento de exceções
@app.exception_handler(AccountNotFoundError)
async def account_not_found_handler(request: Request, exc: AccountNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Account not found."}
    )


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)}
    )
