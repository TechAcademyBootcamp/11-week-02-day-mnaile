from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=125, choices=(('1', 'Convenience Goods'),('2', 'Shopping Goods'),('3', 'Specialty Goods')))
    picture = models.ImageField(upload_to='project_name/media/products/images/')
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    production_date = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=False)
    certificate = models.FileField(upload_to='project_name/media/products/files', null=True,blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True,blank=True)
    detailed_view_link = models.URLField(max_length=300, null=True,blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'company_products'
        ordering = ['name']


    def __str__(self):
        return self.name