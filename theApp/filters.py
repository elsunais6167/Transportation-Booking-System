import django_filters
from .models import *

class tripFilter(django_filters.FilterSet):
    class meta:
        model = Routes
        fields = ['trip']