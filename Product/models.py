from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db import models
from django.conf import settings
from django_extensions.db import fields as extension_fields
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField


class Product(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="media/Product-images/", null=True, blank=True)
    Rest_id = models.CharField(max_length=3,unique=True)

    class Meta:
        ordering = ('category', '-created',)

    def __str__(self):
        return u'%s' % self.Rest_id

    def get_absolute_url(self):
        return reverse('Product_product_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_product_update', args=(self.slug,))


class Order(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=10, null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    address = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)
    delivered_on = models.DateTimeField(blank=True, null=True)
    # Relationship Fields
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, related_name="orders", null=True, blank=True
    )
    order_by = CurrentUserField(blank=True, null=True, related_name="orders_user", on_delete=models.CASCADE)

    class Meta:
        ordering = ('delivered','-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Product_order_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_order_update', args=(self.slug,))


    def save(self, *args, **kwargs):
        if self.delivered:
            if not self.delivered_on:
                self.delivered_on = timezone.now()
        super(Order, self).save(*args, **kwargs)


class Item(models.Model):
    item_id = models.CharField(max_length=3)
    item_name = models.CharField(max_length=15)
    item_desc = models.CharField(max_length=100)
    item_price = models.FloatField(blank=True,null=True)
    item_image = models.ImageField(upload_to="media/Product-images/", null=True, blank=True)
    link_id = models.ForeignKey(Product,to_field='Rest_id',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return u'%s' % self.item_name
    
    def get_absolute_url(self):
        return reverse('Product_Item_detail', args=(self.item_name,))


    def get_update_url(self):
        return reverse('Product_Item_update', args=(self.item_name,))