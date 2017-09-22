from django.core.exceptions import ValidationError
from .models import User

def validate_email_unique(value):
    exist = User.objects.filter(email=value)
    if exists:
        raise ValidationError('Email address %s already exists, must be unique' % value)