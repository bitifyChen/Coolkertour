from django.shortcuts import render
from .models import Area, Tour, SeasonTour


def tour(request):
    foreign = request.GET.get('foreign') == '1'
    areas = Area.objects.filter(foreign=foreign).order_by('sort_index')
    season_tour_tour_ids = [query.get('tour') for query in SeasonTour.objects.all().values('tour')]
    tours = Tour.objects.filter(category__in=areas)\
        .exclude(category__name='活動').exclude(category__name='隱藏').exclude(id__in=season_tour_tour_ids).exclude(hide=True).order_by('-id')
    return render(request, "tour.html", locals())


def tour_detail(request, tour_id):
    query_tour = Tour.objects.filter(id=tour_id)
    side_bar_tours = Tour.objects.all().exclude(category__name='活動').exclude(category__name='隱藏').order_by('-id')[:10]
    if query_tour.exists():
        obj_tour = query_tour.get()
        obj_tour.page_views += 1
        obj_tour.save()
        tours = Tour.objects.filter(category=obj_tour.category).exclude(id=obj_tour.id)[:4]
    return render(request, "tour_detail.html", locals())
