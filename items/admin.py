from django.contrib import admin
from items.models import Category,Items
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']

@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','item_name','image']