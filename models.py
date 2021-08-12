from django.db import models


# Create your models here.
class Product(models.Model):
  
  product_id=  models.AutoField
  product_name=models.CharField(max_length=50)
  desc=        models.CharField(max_length=300)
  pub_date=    models.DateField()
  category=    models.CharField(max_length=50,default="")
  subcategory= models.CharField(max_length=50,default="")
  price=       models.IntegerField(default=0)
  image=       models.ImageField(upload_to="shop/images",default="")
  
  def __str__(self): 
    return self.product_name


class Contact(models.Model): 
  
  name=     models.CharField(max_length=122)
  email=    models.CharField(max_length=122)
  number=   models.CharField(max_length=10)
  message=  models.TextField(max_length=122)

class Orders(models.Model): 
  
  order_id=    models.AutoField(primary_key=True)
  items_json=  models.CharField(max_length=5000)
  name=        models.CharField(max_length=122)
  email=       models.CharField(max_length=122)
  address=     models.CharField(max_length=122)
  city=        models.CharField(max_length=122)
  state=       models.CharField(max_length=122)
  zip_code=    models.CharField(max_length=122)
  
  