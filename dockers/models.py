from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    number = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.number}'
class Docket(models.Model):
    record_type = models.CharField(max_length=255)
    chg = models.CharField(max_length=255, blank=True, null=True)
    com = models.CharField(max_length=255, blank=True, null=True)
    docket_type = models.CharField(max_length=255, blank=True, null=True)
    confirmation = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateField()
    buyer = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    item = models.CharField(max_length=255)
    commodity_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    order_value = models.FloatField()
    amount_invoiced = models.FloatField()
    wbs_code = models.CharField(max_length=255, blank=True, null=True)
    contract = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.po_number

class DocketEntry(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hours_worked = models.FloatField()
    rate_per_hour = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

