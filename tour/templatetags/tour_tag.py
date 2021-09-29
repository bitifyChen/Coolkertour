from django import template
from tour.models import Tour, SeasonTour

register = template.Library()


@register.simple_tag
def get_tour_counts(area_filter):
    season_tour_tour_ids = [query.get('tour') for query in SeasonTour.objects.all().values('tour')]
    return Tour.objects.exclude(category__name='活動').exclude(category__name='隱藏').filter(category__filter=area_filter).exclude(id__in=season_tour_tour_ids).exclude(hide=True).count()
