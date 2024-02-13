from django.contrib import admin
from .models import Organization,Location,BloodDetail, Transaction,Distance
# Register your models here.
admin.site.register(Organization)
admin.site.register(BloodDetail)
admin.site.register(Transaction)
admin.site.register(Location)
admin.site.register(Distance)
