from django.db import models
from django.contrib.auth.models import User

status_choices = (
    (0, "Not Verified"),
    (1, "User Verified"),
    (2, "System Verified"),
    (3, "Rejected")
)

class CityMapping(models.Model):
    id = models.AutoField(primary_key=True)
    supp_city_id = models.CharField(max_length=50, blank=True, null=True)
    supp_city_name = models.CharField(max_length=100, blank=True, null=True)
    supp_dest_code = models.CharField(max_length=50, blank=True, null=True)
    supp_dest_name = models.CharField(max_length=50, blank=True, null=True)
    supp_country_code = models.CharField(max_length=10, blank=True, null=True)
    grn_city_code = models.CharField(max_length=50, blank=True, null=True)
    grn_city_name = models.CharField(max_length=100, blank=True, null=True)
    grn_dest_code = models.CharField(max_length=50, blank=True, null=True)
    grn_dest_name = models.CharField(max_length=100, blank=True, null=True)
    grn_country_code = models.CharField(max_length=50, blank=True, null=True)
    grn_country_name = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True)
    supplier= models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(default=1, choices=status_choices)

    def __str__(self):
        return self.grn_city_name