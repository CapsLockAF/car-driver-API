from django.db import models


class Driver(models.Model):
    """
            This class represents a Driver. \n
            Attributes:
            -----------
            param first_name: Describes first name of the driver
            type first_name: str max_length=128
            param last_name: Describes last name of the driver
            type last_name: str max_length=128
            param created_at: Describes the date when the driver was created. Can't be changed.
            type created_at: int (timestamp)
            param updated_at: Describes the date when the driver was modified
            type updated_at: int (timestamp)
        """
    first_name = models.CharField(blank=True, max_length=128)
    last_name = models.CharField(blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

