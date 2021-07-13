from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from core.models import obras

class obras_form (ModelForm):
    class Meta :
        model=obras
        fields='__all__'

class borrar_form (ModelForm):
    class Meta :
        model=obras
        fields='__all__'

class modificar_form (ModelForm):
    class Meta :
        model=obras
        fields='__all__'