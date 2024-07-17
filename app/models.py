from django.db import models

# Create your models here.
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.color_name}"
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250, null=True, blank=True)
    category_image = models.ImageField(upload_to='category/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.category_name}'
# Modeli mund te jete per sherbime, produkete specifike
# Ture, paketa, evente, prona, agjent, kontakt,
# subscribe, booking, hotele, restorante,  etj
class Product(models.Model):
    product_title = models.CharField(max_length=250, null=True, blank=True )
    product_description = models.TextField(max_length=2000, null=True, blank=True)
    product_week = models.IntegerField(null=True, blank=True)
    product_hours = models.FloatField(null=True, blank=True)
    product_image = models.ImageField(upload_to="product/", null=True, blank=True)
    product_slug = models.SlugField(unique=True,  null=True, blank=True)
    product_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    product_color = models.ManyToManyField(Color, blank=True)
    
    def __str__(self):
        return f"{self.product_title} "
    
    
class FormContact(models.Model):
    formContact_name = models.CharField(max_length=250, null=True, blank=True)
    formContact_surname = models.CharField(max_length=250, null=True, blank=True)
    formContact_email = models.EmailField(null=True, blank=True)
    formContact_comment = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.formContact_name} {self.formContact_surname}"