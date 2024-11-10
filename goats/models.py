from django.db import models

class Goat(models.Model):
    tag_no = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    health_status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    sire_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sire_offspring')
    dam_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='dam_offspring')
    update_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.tag_no} - {self.name}"

class HistoricalGoat(models.Model):
    goat = models.ForeignKey(Goat, on_delete=models.CASCADE, related_name='history')
    tag_no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    health_status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    update_date = models.DateTimeField()

    def __str__(self):
        return f"History for {self.goat.name} at {self.change_date}"
