# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def BootstrapFilterView(request):
    return render(request, 'bootstrap_form.html', {})
