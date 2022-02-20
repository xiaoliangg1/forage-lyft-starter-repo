from abc import ABC

from tires import tires


class WilloughbyEngine(tires, ABC):
    def __init__(self, last_service_date, tire):
        super().__init__(last_service_date, tire)

    def tires_should_be_serviced(self):
        sum = 0
        for i in self.tires:
            sum += i
        if sum >= 3:
            return False
        return True