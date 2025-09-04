from django.db import models

# Create your models here.


class Item(models.Model):
    itemname = models.CharField(max_length=180)
    itemPrice = models.IntegerField()
    itemImage = models.ImageField(upload_to='items/')

    def _str_(self):
        return self.itemname
