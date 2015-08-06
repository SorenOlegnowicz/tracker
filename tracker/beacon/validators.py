from django.core.exceptions import ValidationError


def validate_pin(value):
    for i in value:
        if i.isdigit == False:
            raise ValidationError('{} is not a 4 digit pin number'.format(value))