from django.db import models
from django.conf import settings

class Complaint(models.Model):
    STATUS_CHOICES = (('pending','Pending'),('approved','Approved'),('rejected','Rejected'))
    retailer_name = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    feedback_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.retailer_name} - {self.customer_name}"