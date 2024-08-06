from django.db import models

# Create your models here.

# Modeli mund te jete per sherbime, produkete specifike
# Ture, paketa, evente, prona, agjent, kontakt,
# subscribe, booking, hotele, restorante,  etj
class Product(models.Model):
    product_title = models.CharField(max_length=250, null=True, blank=True )
    product_description = models.TextField(max_length=2000, null=True, blank=True)
    product_image = models.ImageField(upload_to="product/", null=True, blank=True)
    product_slug = models.SlugField(unique=True,  null=True, blank=True)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
   
    def __str__(self):
        return f"{self.product_title} "
    
    
class FormContact(models.Model):
    formContact_name = models.CharField(max_length=250, null=True, blank=True)
    formContact_surname = models.CharField(max_length=250, null=True, blank=True)
    formContact_email = models.EmailField(null=True, blank=True)
    formContact_comment = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.formContact_name} {self.formContact_surname}"