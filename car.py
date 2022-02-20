from abc import ABC, abstractmethod

import serviceable


class Car(serviceable, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    @abstractmethod
    def needs_service(self):
        pass
