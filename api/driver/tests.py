import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from driver.models import Driver
from vehicle.models import Vehicle
from .views import *

import datetime
from unittest import mock

import pytz

TEST_DATE_LTE = datetime.datetime(2021, 12, 8, 12, 00, tzinfo=pytz.utc)
TEST_DATE_GTE = datetime.datetime(2021, 12, 12, 12, 00, tzinfo=pytz.utc)


class TestDriverModel(TestCase):
    """Class for Driver Model API test"""
    def setUp(self):
        """ Create a driver object to be used by the tests """
        time_mock = TEST_DATE_LTE
        with mock.patch('django.utils.timezone.now') as mock_time:
            mock_time.return_value = time_mock
            self.factory = APIRequestFactory()

            self.driver1 = Driver(id=101,
                                  first_name="John",
                                  last_name="Doe",
                                  )
            self.driver1.save()
            self.driver2 = Driver(id=102,
                                  first_name="Anna",
                                  last_name="Corry",
                                  )
            self.driver2.save()

    def test_get_list_status_code_200(self):
        request = self.factory.get('/drivers/driver/')
        response = drivers_list(request)
        self.assertEqual(response.status_code, 200)

    def test_post_driver_status_code_201(self):
        new_driver = {
            "first_name": "Michel",
            "last_name": "Kideman"
        }
        request = self.factory.post('/drivers/driver/', new_driver, format='json')
        response = drivers_list(request)
        self.assertEqual(response.status_code, 201)

