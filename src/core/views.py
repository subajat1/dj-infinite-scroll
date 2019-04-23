from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render

from .models import Journal

def BootstrapFilterView(request):
    qs = Journal.objects.all()

    title_contains_query = request.GET.get('title_contains')
    title_exact_query = request.GET.get('title_exact')
    title_or_author_query = request.GET.get('title_or_author')

    if not title_contains_query in (None, ''):
        qs = qs.filter(title__icontains=title_contains_query)

    elif not title_exact_query in (None, ''):
        qs = qs.filter(title__iexact=title_exact_query)

    elif not title_or_author_query in (None, ''):
        qs = qs.filter( Q(title__icontains=title_or_author_query) 
                      | Q(author__name__icontains=title_contains_query)
                      ).distinct()

    context = {
        'queryset': qs
    }

    return render(request, 'bootstrap_form.html', context)
