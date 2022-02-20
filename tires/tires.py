from abc import ABC, abstractmethod

from car import Car


class Engine(Car, ABC):
    def __init__(self, last_service_date, tire):
        super().__init__(last_service_date)
        self.tires = tire

    @abstractmethod
    def tires_should_be_serviced(self):
        pass