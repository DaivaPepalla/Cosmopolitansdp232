from django.db import models
from django.db.models.functions import datetime
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'menu'

    def get_absolute_url(self):
        return reverse("store:categorymenu",args=[self.slug])

    def __str__(self):
        return self.name

class Items(models.Model):
    menu = models.ForeignKey(Menu, related_name='item', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='item_creator')
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)    
    
    class Meta:
        verbose_name_plural = 'Items'

    def get_absolute_url(self):
        return reverse('store:eachitem',args=[self.slug])

    def __str__(self):
        return self.item_name

class Nonveg(models.Model):
    menu = models.ForeignKey(Menu, related_name='nonvegitem', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    status=models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'nonveg'

    def get_absolute_url(self):
        return reverse('store:eachitem',args=[self.slug])

    def __str__(self):
        return self.name

class Veg(models.Model):
    menu = models.ForeignKey(Menu, related_name='vegitem', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    status=models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'veg'

    def get_absolute_url(self):
        return reverse('store:eachitem',args=[self.slug])

    def __str__(self):
        return self.name
    
class Beverages(models.Model):
    menu = models.ForeignKey(Menu, related_name='beverageitem', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    status=models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'beverages'

    def get_absolute_url(self):
        return reverse('store:eachitem',args=[self.slug])

    def __str__(self):
        return self.name

class Desserts(models.Model):
    menu = models.ForeignKey(Menu, related_name='dessertitem', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    status=models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'desserts'

    def get_absolute_url(self):
        return reverse('store:eachitem',args=[self.slug])

    def __str__(self):
        return self.name

class Gallery1(models.Model):
    name = models.CharField(max_length=255,db_index=True)

    class Meta:
        verbose_name_plural = 'gallery1'

    def __str__(self):
        return self.name

class Gallery2(models.Model):
    category = models.ForeignKey(Gallery1, related_name='gallerytype', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,db_index=True,default='abc') 
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'gallery2'

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'contactus'

    def __str__(self):
        return self.name

class allItems(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    time = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    class Meta:
        verbose_name_plural = 'allitems'

    def __str__(self):
        return self.name
    @staticmethod
    def get_products_by_id(ids):
        return allItems.objects.filter(name__in=ids)



class Check(models.Model):
    username = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    streetaddress=models.CharField(max_length=255,default='abc')
    locality=models.CharField(max_length=255,default='abc')
    city=models.CharField(max_length=255,default='abc')
    pincode=models.IntegerField()
    phone=models.IntegerField()

    def __str__(self):
        return self.username


class Order(models.Model):
    item=models.ForeignKey(allItems, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    quantity=models.IntegerField(default=1)
    comment = models.CharField(max_length=255,default='')
    price=models.IntegerField()
    streetaddress = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    phone=models.IntegerField()
    total=models.IntegerField()
    date=models.DateField(default=datetime.datetime.now)
    status=models.BooleanField(default=False)
    resprepstatus=models.BooleanField(default=True)
    deliverystatus=models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(user):
        return Order.objects.filter(username=user)
    @staticmethod
    def delete(id):

            Order.objects.filter(id=id).delete()


class Pay(models.Model):
    name=models.CharField(max_length=255)
    cardno=models.IntegerField()
    cardname=models.CharField(max_length=255)
    cvv=models.IntegerField()
    expmonth=models.IntegerField()
    expyr=models.IntegerField()


class RoomCheck(models.Model):
    username = models.CharField(max_length=255)
    streetaddress=models.CharField(max_length=255,default='abc')
    locality=models.CharField(max_length=255,default='abc')
    city=models.CharField(max_length=255,default='abc')
    pincode=models.IntegerField()
    phone=models.IntegerField()


class Room(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description=models.CharField(max_length=255)
    price = models.IntegerField(default='0')
    stars = models.IntegerField(default='0')
    adult=models.IntegerField(default=0)
    children=models.IntegerField(default=0)
    @staticmethod
    def get_all_rooms():
        return Room.objects.all()
    @staticmethod
    def get_products_by_id(ids):
        return Room.objects.filter(id__in=ids)


class RoomOrder(models.Model):
    item=models.ForeignKey(Room, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    checkin=models.CharField(max_length=50)
    price=models.IntegerField()
    days=models.IntegerField()
    adult=models.IntegerField()
    children=models.IntegerField()
    streetaddress = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    phone=models.IntegerField()
    total=models.IntegerField()
    date=models.DateField(default=datetime.datetime.now)
    def placeRoomOrder(self):
        self.save()
    @staticmethod
    def get_Roomorders_by_customer(user):
        return RoomOrder.objects.filter(username=user)
