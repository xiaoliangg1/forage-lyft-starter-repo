from abc import ABC, abstractmethod

import serviceable


class Car(serviceable, ABC):
    def __init__(self, last_service_date, tires):
        super().__init__(last_service_date)
        self.tires = tires

    @abstractmethod
    def needs_service(self):
        pass
