from django_filters import widgets, FilterSet, DateFromToRangeFilter, RangeFilter, DateFilter
from django import forms
from .models import Post

class PostFilter(FilterSet):
    pub_time__gt = DateFilter(
        field_name='publication_date',
        label='Start date',
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        lookup_expr='date__gte'
    )

    class Meta:
        model = Post
        fields = {
            'post_name': ['icontains'],
            'author': ['exact'],
}