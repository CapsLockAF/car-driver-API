from django.db import models
from driver.models import Driver

from django.core.validators import RegexValidator


class Vehicle(models.Model):
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
                                    validators=[plate_num_validator]
                                    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


