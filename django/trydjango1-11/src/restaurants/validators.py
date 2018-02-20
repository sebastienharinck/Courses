from django.core.exceptions import ValidationError


CATEGORIES = ['Mexican', 'American', 'Asian', 'Whatever']


def validate_category(value):
    cat = value.capitalize()
    if cat not in CATEGORIES:
        raise ValidationError(f'{value} is not a valid category.')
