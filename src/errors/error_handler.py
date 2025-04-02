from src.views.http_types.http_response import HttpResponse
from .error_type.http_bad_request import HtppBadRequestError
from .error_type.http_not_found import HtppNotFoundError
from .error_type.http_unprocessable_entity import HtppUnprocessableEntityError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HtppBadRequestError, HtppNotFoundError, HtppUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
