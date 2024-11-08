from django.shortcuts import render, redirect, get_object_or_404
from .models import Goat
from .forms import GoatForm

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
