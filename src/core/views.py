from __future__ import unicode_literals

from django.shortcuts import render

from .models import Journal

def BootstrapFilterView(request):
    qs = Journal.objects.all()

    title_contains_query = request.GET.get('title_contains')
    title_exact_query = request.GET.get('title_exact')
    title_or_author_query = request.GET.get('title_or_author')
    context = {
        'queryset': qs
    }

    return render(request, 'bootstrap_form.html', context)
