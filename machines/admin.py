from django.contrib import admin
from .models import Developer, Category, Manufacturing, ProductionArea, Machine, Value

admin.site.register(Manufacturing)
admin.site.register(ProductionArea)
admin.site.register(Developer)
admin.site.register(Category)
admin.site.register(Machine)
admin.site.register(Value)
