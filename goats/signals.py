from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Goat, HistoricalGoat

@receiver(pre_save, sender=Goat)
def save_goat_history(sender, instance, **kwargs):
    if instance.pk:  # Only save if the goat exists (not a new creation)
        current_data = Goat.objects.get(pk=instance.pk)
        HistoricalGoat.objects.create(
            goat=instance,
            tag_no=current_data.tag_no,
            name=current_data.name,
            breed=current_data.breed,
            dob=current_data.dob,
            gender=current_data.gender,
            weight=current_data.weight,
            health_status=current_data.health_status,
            location=current_data.location,
            status=current_data.status,
            update_date=current_data.update_date,
        )
