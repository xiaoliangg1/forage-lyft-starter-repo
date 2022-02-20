from abc import ABC

from engine import engine


class CapuletEngine(engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, tiers):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.tiers = tires

    def engine_should_be_serviced(self):
        count = 0
        for i in self.tires:
            if i >= 0.9:
                count += 1
        return self.current_mileage - self.last_service_mileage > 30000 and count >= 1
