import django_filters
from apps.games.models.games import Tags, Game


class GameFilter(django_filters.FilterSet):
    order_by_price = django_filters.ChoiceFilter(
        method='filter_by_price',
        label='Сортировка по цене',
        choices=(
            ('desc', 'Сначала дорогие'),
            ('asc', 'Сначала дешевые'),
        ),
    )
    price = django_filters.RangeFilter(field_name='price')

    tags = django_filters.ModelMultipleChoiceFilter(field_name='tags', queryset=Tags.objects.all())

    class Meta:
        model = Game
        fields = ['order_by_price', 'price', 'tags']
        
    def filter_by_price(self, queryset, name, value):
        if value == 'desc':
            return queryset.order_by('-price')
        elif value == 'asc':
            return queryset.order_by('price')
        else:
            return queryset
