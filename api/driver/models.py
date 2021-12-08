from django.db import models, DataError, IntegrityError
from django.core.validators import RegexValidator
import datetime


class Driver(models.Model):
    first_name = models.CharField(blank=True, max_length=64)
    last_name = models.CharField(blank=True, max_length=64)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

