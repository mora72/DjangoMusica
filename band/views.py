from django.shortcuts import render, get_object_or_404
from .models import Band


def indexband(request):
    return render(request, 'band.html')


def detail(request, band_id):
    # band = Band.objects.get(pk=band_id)
    band = get_object_or_404(Band, pk=band_id)
    return render(request, 'detail.html', {'band': band})
