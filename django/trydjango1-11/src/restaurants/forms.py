from django import forms

from .models import Restaurant
from .validators import validate_category


class RestaurantCreateForm(forms.ModelForm):
    category = forms.CharField(validators=[validate_category], required=False)

    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'category']
