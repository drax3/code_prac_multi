from django.db import models
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
    cat        = models.CharField(max_length=150)
    birth_year = models.IntegerField()
    img        = models.FileField(upload_to='cat/images', blank=True)

    def __str__(self):
        return self.cat
    
    def get_absolute_url(self):
        return reverse('cat_detail', args=[str(self.id)])