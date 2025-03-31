from ...controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse


class PetDeleterView():
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controller.delete(name)

        return HttpResponse(status_code=204)
