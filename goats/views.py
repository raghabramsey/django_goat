from django.shortcuts import render, redirect, get_object_or_404
from .models import Goat,HistoricalGoat
from .forms import GoatForm
from .forms import GoatUpdateForm
from django.utils import timezone


def goat_update(request, goat_id):
    goat = get_object_or_404(Goat, id=goat_id)
    
    if request.method == 'POST':
        form = GoatUpdateForm(request.POST, instance=goat)
        if form.is_valid():
            # Save the previous state to history
            HistoricalGoat.objects.create(
                goat=goat,
                name=goat.name,
                breed=goat.breed,
                dob=goat.dob,
                gender=goat.gender,
                weight=goat.weight,
                health_status=goat.health_status,
                location=goat.location,
                status=goat.status,
                update_date=timezone.now(),
            )
            # Save the updated goat
            form.save()
            return redirect('goat_detail', goat_id= goat.id)

    else:
        form = GoatUpdateForm(instance=goat)
    
    return render(request, 'goats/update_goat.html', {'form': form, 'goat': goat})


def register_goat(request):
    if request.method == 'POST':
        form = GoatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goat_list')
        
    else:
        form = GoatForm()
    return render(request, 'goats/register_goat.html', {'form': form})

def goat_list(request):
    goats = Goat.objects.all()
    return render(request, 'goats/goat_list.html', {'goats': goats})

def goat_detail(request, goat_id):
    goat = get_object_or_404(Goat, pk=goat_id)
    return render(request, 'goats/goat_detail.html', {'goat': goat})


def goat_history(request, goat_id):
    # Get all history entries for the specified goat
    history_entries = HistoricalGoat.objects.filter(goat_id=goat_id).order_by('-update_date')
    return render(request, 'goats/goat_history.html', {'history_entries': history_entries})
