# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customers(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class EmployeePrivileges(models.Model):
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    privilege = models.ForeignKey('Privileges', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_privileges'
        unique_together = (('employee', 'privilege'),)


class Employees(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class InventoryTransactionTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'inventory_transaction_types'


class InventoryTransactions(models.Model):
    transaction_type = models.ForeignKey(InventoryTransactionTypes, models.DO_NOTHING, db_column='transaction_type')
    transaction_created_date = models.DateTimeField(blank=True, null=True)
    transaction_modified_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.IntegerField()
    purchase_order = models.ForeignKey('PurchaseOrders', models.DO_NOTHING, blank=True, null=True)
    customer_order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_transactions'


class Invoices(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    tax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shipping = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    amount_due = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class OrderDetails(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=4)
    unit_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discount = models.FloatField()
    status = models.ForeignKey('OrderDetailsStatus', models.DO_NOTHING, blank=True, null=True)
    date_allocated = models.DateTimeField(blank=True, null=True)
    purchase_order_id = models.IntegerField(blank=True, null=True)
    inventory_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_details'


class OrderDetailsStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'order_details_status'


class Orders(models.Model):
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    shipped_date = models.DateTimeField(blank=True, null=True)
    shipper = models.ForeignKey('Shippers', models.DO_NOTHING, blank=True, null=True)
    ship_name = models.CharField(max_length=50, blank=True, null=True)
    ship_address = models.TextField(blank=True, null=True)
    ship_city = models.CharField(max_length=50, blank=True, null=True)
    ship_state_province = models.CharField(max_length=50, blank=True, null=True)
    ship_zip_postal_code = models.CharField(max_length=50, blank=True, null=True)
    ship_country_region = models.CharField(max_length=50, blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    taxes = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    tax_status = models.ForeignKey('OrdersTaxStatus', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('OrdersStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orders_status'


class OrdersTaxStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    tax_status_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orders_tax_status'


class Privileges(models.Model):
    privilege_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'privileges'


class Products(models.Model):
    supplier_ids = models.TextField(blank=True, null=True)
    product_code = models.CharField(max_length=25, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    standard_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    list_price = models.DecimalField(max_digits=19, decimal_places=4)
    reorder_level = models.IntegerField(blank=True, null=True)
    target_level = models.IntegerField(blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=50, blank=True, null=True)
    discontinued = models.IntegerField()
    minimum_reorder_quantity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class PurchaseOrderDetails(models.Model):
    purchase_order = models.ForeignKey('PurchaseOrders', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=4)
    unit_cost = models.DecimalField(max_digits=19, decimal_places=4)
    date_received = models.DateTimeField(blank=True, null=True)
    posted_to_inventory = models.IntegerField()
    inventory = models.ForeignKey(InventoryTransactions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_details'


class PurchaseOrderStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_status'


class PurchaseOrders(models.Model):
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(Employees, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    submitted_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(PurchaseOrderStatus, models.DO_NOTHING, blank=True, null=True)
    expected_date = models.DateTimeField(blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=19, decimal_places=4)
    taxes = models.DecimalField(max_digits=19, decimal_places=4)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    submitted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_orders'


class SalesReports(models.Model):
    group_by = models.CharField(primary_key=True, max_length=50)
    display = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    filter_row_source = models.TextField(blank=True, null=True)
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_reports'


class Shippers(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippers'


class Strings(models.Model):
    string_id = models.AutoField(primary_key=True)
    string_data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strings'


class Suppliers(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'
