from logging import Logger
from time import perf_counter

from fastapi import Request, Response, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        response: Response = await call_next(request)
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
            "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
            "img-src 'self' data: https://fastapi.tiangolo.com; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "frame-ancestors 'none';"
        )
        return response


def add_middlewares(app: FastAPI, logger: Logger) -> None:
    @app.middleware("http")
    async def measure_request_time(
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        start_time = perf_counter()
        response = await call_next(request)
        process_time = f"{perf_counter() - start_time:.4f}"

        response.headers["X-Process-Time"] = process_time
        logger.info(
            "Request %s %s completed with status %s in %s seconds",
            request.method,
            request.url.path,
            response.status_code,
            process_time,
        )
        return response
