from typing import Dict
from src.errors.error_type.http_not_found import HtppNotFoundError
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def find(self, person_id:int) -> Dict:
        person = self.__find_person_ind_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_ind_db(self, person_id:int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HtppNotFoundError("Pessoa não encontrada!")

        return person

    def __format_response(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pe_name": person.pet_name,
                    "pet_type": person.pet_type
                }
            }
        }
