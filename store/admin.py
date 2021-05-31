from django.contrib import admin
from .models import Items,Menu,Nonveg, Pay,Veg,Beverages,Desserts,Gallery1,Gallery2,Contactus,Check,allItems,Order,Pay,Room,RoomCheck,RoomOrder

# Register your models here.
admin.site.register(Order)
admin.site.register(allItems)
admin.site.register(Check)
admin.site.register(Pay)
admin.site.register(Room)
admin.site.register(RoomCheck)
admin.site.register(RoomOrder)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['item_name','price','slug']
    list_editable = ['price']
    prepopulated_fields = {'slug':('item_name',)}

@admin.register(Nonveg)
class NonvegAdmin(admin.ModelAdmin):
    list_display = ['name','price','slug','description','time']
    list_editable = ['price','description','time']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Veg)
class VegAdmin(admin.ModelAdmin):
    list_display = ['name','price','slug','description','time']
    list_editable = ['price','description','time']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Beverages)
class BeveragesAdmin(admin.ModelAdmin):
    list_display = ['name','price','slug','description','time']
    list_editable = ['price','description','time']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Desserts)
class DessertsAdmin(admin.ModelAdmin):
    list_display = ['name','price','slug','description','time']
    list_editable = ['price','description','time']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Gallery1)
class Gallery1Admin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Gallery2)
class Gallery2Admin(admin.ModelAdmin):
    list_display = ['category','name']
    list_editable = ['name']

@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']
    list_editable = ['email','message']
    
