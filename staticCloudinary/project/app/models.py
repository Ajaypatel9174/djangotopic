from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage,MediaCloudinaryStorage,VideoMediaCloudinaryStorage

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='image/', storage=MediaCloudinaryStorage)
    vidio = models.FileField( upload_to='file/' , storage=VideoMediaCloudinaryStorage)
    audio = models.FileField( upload_to='file/' ,   storage=VideoMediaCloudinaryStorage)

    
