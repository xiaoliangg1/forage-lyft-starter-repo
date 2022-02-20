from abc import ABC

from tires import tires


class Carrigan_tires(tires, ABC):
    def __init__(self, last_service_date, tire):
        super().__init__(last_service_date, tire)

    def tires_should_be_serviced(self):
        for i in self.tires:
            if i >= 0.9:
                return False
        return True
