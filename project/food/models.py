from django.db import models

# Create your models here.
class item(models.Model):
    def __str__(self):
        return self.food_name 
    food_name= models.CharField(max_length=200)
    food_description=models.CharField()
    food_price= models.IntegerField()
    food_image=models.CharField(default='https://toppng.com/uploads/preview/clipart-free-seaweed-clipart-draw-food-placeholder-11562968708qhzooxrjly.png')
