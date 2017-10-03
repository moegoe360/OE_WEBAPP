import re
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

# from .models import User
# 
# def validate_email_unique(value):
#     exist = User.objects.filter(email=value)
#     if exists:
#         raise ValidationError('Email address %s already exists, must be unique' % value)
    
@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0