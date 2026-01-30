from django.forms import ModelForm
from .models import item

class add_item(ModelForm):
    class Meta:
        model=item
        fields=['food_name', 'food_description', 'food_price', 'food_image']