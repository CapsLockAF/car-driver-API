from django.db import models
from driver.models import Driver

from django.core.validators import RegexValidator


class Vehicle(models.Model):
    """
                This class represents a Vehicle. \n
                Attributes:
                -----------
                param driver_id: The driver in a vehicle
                type driver_id: null or int:driver.id
                param make: Describes the country or the company that made  the vehicle
                type make: str max_length=128
                param model: Describes a model or the vehicle
                type model: str max_length=128
                param plate_number: A plate number of the vehicle. AA 1234 OO
                type plate_number: str max_length=10 validated
                param created_at: Describes the date when the vehicle was created. Can't be changed.
                type created_at: int (timestamp)
                param updated_at: Describes the date when the vehicle was modified
                type updated_at: int (timestamp)
            """
    driver_id = models.ForeignKey(Driver,
                                  models.SET_NULL,
                                  blank=True,
                                  null=True
                                  )
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)

    plate_num_validator = RegexValidator(
        regex=r"\b[A-Z]{2}\s[0-9]{4}\s[A-Z]{2}\b",
        message="Incorrect number. Please use "
                "the following format: AA 1234 OO"
    )
    plate_number = models.CharField(max_length=10,
                                    help_text="Please use the following "
                                              "format: <em>AA 1234 OO</em>"
                                              ".",
                                    validators=[plate_num_validator],
                                    unique=True
                                    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.make} ' \
               f'{self.model} {self.plate_number} {self.driver_id}'

