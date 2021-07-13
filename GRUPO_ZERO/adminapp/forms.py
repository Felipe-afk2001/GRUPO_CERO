from django import forms
from django.db import models
from django.forms import ModelForm
from core.models import obras

class obras_form (ModelForm):
    class Meta :
        model=obras
        fields='__all__'