from django.core.cache import caches
from django.shortcuts import render


def hitme(request):
    cache = caches['hits']
    try:
        hits = cache.incr('hits')
    except ValueError:
        cache.set('hits', 1)
        hits = 1
    return render(request, 'hits/hitme.html', {'hits': hits})
