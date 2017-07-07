from django.contrib import admin

from models import Customers, Orders

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('company', 'last_name','first_name','email_address',
                    'job_title')



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('tax_rate',)
