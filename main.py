# Main entry point of the Call Center project.

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from routes.calls import router as calls_router
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.include_router(calls_router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid request"}
    )


@app.get("/")
def root():
    return {"message": "Call Center API is running"}