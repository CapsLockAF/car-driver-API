## Getting started
Please follow the instructions below.

Run manually:
```commandline
git clone REPO
cd REPO
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

cd api
python manage.py migrate
python manage.py runserver
```
You can then visit localhost*** to verify that it's running on your machine.
##Available Routes
```
Driver:
+ GET /drivers/driver/ - retrieve a list of drivers
+ GET /drivers/driver/?created_at__gte=10-11-2021 - the output of 
+ the list of drivers who are created after 16-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - the output of 
+ the list of drivers who are created till 16-11-2021

+ GET /drivers/driver/<driver_id>/ - retrieving information on a specific driver
+ POST /drivers/driver/ - creating a driver
+ UPDATE /drivers/driver/<driver_id>/ - editing the driver
+ DELETE /drivers/driver/<driver_id>/ - remove the driver

Vehicle:
+ GET /vehicles/vehicle/ - retrieve a list of vehicles
+ GET /vehicles/vehicle/?with_drivers=yes - retrieve a list of vehicles with drivers
+ GET /vehicles/vehicle/?with_drivers=no - retrieve a list of vehicles without drivers

+ GET /vehicles/vehicle/<vehicle_id> - retrieving information on a specific vehicle
+ POST /vehicles/vehicle/ - creating a vehicle
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - editing the vehicle
+ POST /vehicles/set_driver/<vehicle_id>/ - we put the driver in the car /
+ we put the driver out of the car  
+ DELETE /vehicles/vehicle/<vehicle_id>/ - remove the vehicle```

Also, you can use admin panel `admin/` with credentials:
```commandline
name: admin
password: 123456789
```