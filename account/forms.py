from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Crmuser, BatteryDetail
from django import forms
from django.contrib.auth import get_user_model

from django.views.generic import CreateView
from django.forms import ModelForm


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Crmuser
        fields = ['username','email','contact','password','password_conformation']

class BatteryDetailsFrom(forms.ModelForm):
    class Meta:
        model = BatteryDetail
        fields = ['model_name','battery_serial_num','battery_type','bms_type','iot_type',
                  'iot_imei_number','sim_number','warrenty_start_date','warrenty_end_date',
                  'assigned_owner','status','battery_cell_chemistry','battery_pack_nominal_voltage',
                  'battery_pack_nominal_charge_capacity','charging_status']
        # labels = {
        #     'model_name': 'MODEL_NAME',
        #     'battery_type': 'BATTERY_TYPE'
        # }
    def __init__(self, *args, **kwargs):
        super(BatteryDetailsFrom,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select"
        self.fields['model_name'].empty_label = "Select"
        self.fields['bms_type'].empty_label = "Select"
        self.fields['battery_serial_num'].required = True