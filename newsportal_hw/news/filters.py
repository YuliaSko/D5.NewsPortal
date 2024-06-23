from django_filters import (
    FilterSet, CharFilter, ModelChoiceFilter, DateFilter
)
from .models import Post, Author
from django.forms import DateInput


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все авторы'
    )

    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название поста'
    )

    date_post = DateFilter(
        field_name='date_post',
        lookup_expr='gt',
        label='Публикации после',
        widget=DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = {
            'author',
            'title',
            'date_post',
        }
