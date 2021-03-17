from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
"""from .models import """
from django.db import transaction, IntegrityError

# Create your views here.
def index(request):
    return render(request, 'carPieces/index.html')
