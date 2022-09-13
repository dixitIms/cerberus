from django.db import models
from datetime import datetime

# Create your models here.

class Crmuser(models.Model):
    username = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=20,default='', primary_key=True)
    contact = models.CharField(max_length=12, default='')
    age = models.CharField(max_length=2, default='')
    password = models.CharField(max_length=20,default='')
    password_conformation = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.username + " " + self.email

MODEL_CHOICES = (
    ('igtblu','IGTBLU'),
    ('igtred','IGTRED'),
    ('igtred+','IGTRED+'),
)

BATTERY_TYPES = (
    ('1','24'),
    ('2','48'),
    ('3','60'),
    ('4','72'),
)

BMS_TYPE = (
    ('ion', 'ION'),
    ('electrifuel', 'ELECTRIFUEL'),
)

IOT_TYPE = (
    ('tarckmate', 'TRACKMATE'),
    ('electrifuel', 'ELECTRIFUEL'),
    ('aeidth', 'AEIDTH'),
)

STATUS = (
    ('in_swap_station', 'IN_SWAP_STATION'),
    ('in_vehicle', 'IN_VEHICLE'),
    ('idel', 'IDEL'),
    ('damaged','DAMAGED'),
)

class BatteryDetail(models.Model):
    model_name = models.CharField(max_length=100,default='', choices=MODEL_CHOICES)
    battery_serial_num = models.CharField(max_length=100, primary_key=True, default='', unique=True)
    battery_type = models.CharField(max_length=100, default='', unique=True, choices=BATTERY_TYPES)
    bms_type = models.CharField(max_length=100, default='', choices=BMS_TYPE)
    iot_type = models.CharField(max_length=100, default='', choices=IOT_TYPE)
    iot_imei_number = models.CharField(max_length=1000)
    sim_number = models.CharField(max_length=12, default='', blank=True)
    warrenty_start_date = models.DateTimeField(default=datetime.now,blank=True)
    warrenty_end_date = models.DateTimeField(default=datetime.now,blank=True)
    assigned_owner = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    battery_cell_chemistry = models.CharField(max_length=50, default='')
    battery_pack_nominal_voltage = models.CharField(max_length=50, default='')
    battery_pack_nominal_charge_capacity = models.CharField(max_length=50, default='')
    charging_status = models.CharField(max_length=50, default=False, null=True)


    def __str__(self):
        return str(self.model_name)



