from abc import ABC

from battery import battery

class SpindlerBattery(battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def engine_should_be_serviced(self):
        return self.current_date - self.last_service_date > 60000