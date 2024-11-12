import django_filters
from .models import Job



class JobFilter(django_filters.FilterSet):
    # means that when u search for django then return all jobs which its description contains this word django
    # description = django_filters.CharFilter(lookup_expr='iexact') if u want to (iexact)
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = [ 'owner' , 'image' , 'salary' , 'published_at' , 'Vacancy' , 'slug']