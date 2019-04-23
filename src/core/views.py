from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render

from .models import Category, Journal

def is_valid_queryparam(param):
    return param != '' and param is not None

def BootstrapFilterView(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_exact_query = request.GET.get('title_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('not_reviewed')

    if not title_contains_query in (None, ''):
        qs = qs.filter(title__icontains=title_contains_query)

    elif not title_exact_query in (None, ''):
        qs = qs.filter(title__iexact=title_exact_query)

    elif not title_or_author_query in (None, ''):
        qs = qs.filter( Q(title__icontains=title_or_author_query) 
                      | Q(author__name__icontains=title_contains_query)
                      ).distinct()

    if not view_count_min in (None, ''):
        qs = qs.filter(views__gte=view_count_min)

    if not view_count_max in (None, ''):
        qs = qs.filter(views__lt=view_count_max)

    if not date_min in (None, ''):
        qs = qs.filter(publish_date__gte=date_min)

    if not date_max in (None, ''):
        qs = qs.filter(publish_date__lt=date_max)

    if not category in (None, '') and category != 'Choose...':
        qs = qs.filter(categories__name=category)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)
    elif not_reviewed == 'on':
        qs = qs.filter(reviewed=False)


    context = {
        'queryset': qs,
        'categories': categories,
    }

    return render(request, 'bootstrap_form.html', context)
