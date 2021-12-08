from django.db import models, DataError, IntegrityError
from django.core.validators import RegexValidator
import datetime

from driver.models import Driver


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver,
                                  models.SET_NULL,
                                  blank=True,
                                  null=True
                                  )
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    plate_number = models.CharField(max_length=10,
                                    help_text="Please use the following "
                                              "format: <em>AA 1234 OO</em>"
                                              ".")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


