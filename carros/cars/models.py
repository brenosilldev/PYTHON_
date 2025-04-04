from django.db import models # type: ignore


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Car(models.Model):
    id = models.AutoField(primary_key=True)  
    model = models.CharField(max_length=100,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='car_brand')
    factroy_year = models.IntegerField(blank=True,null=True)
    model_year = models.IntegerField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    photo = models.ImageField(upload_to='cars/',blank=True,null=True)


    def __str__(self):
        return self.model