from django.contrib import admin
from  goods.models import  TypeInfo
from  goods.models import GoodsInfo
# Register your models here.

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['gtitle','gpic','gprice','gunit','gclick','gsaleCount','gjianjie','gkucun','gcontent','gtype']


admin.site.register(TypeInfo)
admin.site.register(GoodsInfo)