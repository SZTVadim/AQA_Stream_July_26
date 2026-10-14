import random
import uuid
from dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    middle_name: str
    last_name: str
    employee_id: str

    @classmethod
    def generate_employee(cls):
        suffix = random.randint(1000, 9999)
        return Employee(
            first_name=f'first_{suffix}',
            middle_name=f'middle_{suffix}',
            last_name=f'last_{suffix}',
            employee_id= str(uuid.uuid4().int)[:6]
        )