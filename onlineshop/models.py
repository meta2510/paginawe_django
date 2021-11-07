from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('onlineshop:product_list_by_category',
        args=[self.slug])

class Product(models.Model):

    TIENDAS = (
        ('Miraflores', 'Miraflores'),
        ('Tikal Futura', 'Tikal Futura'),
        ('Eskala Roosevelt', 'Eskala Roosevelt'),
    )
    
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='productos',null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avaible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    inventory = models.IntegerField(default=0)
    tienda = models.CharField(choices=TIENDAS, max_length=16)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def item_sold(self, save=True):
	    current_inv = self.inventory
	    current_inv -= 1
	    self.inventory = current_inv
	    if save == True:
		    self.save()
	    return self.inventory

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('onlineshop:product_detail',
        args=[self.id,self.slug])
