from django.shortcuts import render
from django.db.models import Prefetch
from .models import Article, Scope

def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'

    articles = Article.objects.prefetch_related(
        Prefetch(
            'scopes',
            queryset=Scope.objects.order_by('-is_main', 'tag__name'),
            to_attr='ordered_scopes'
        )
    ).order_by(ordering)

    context = {'object_list': articles}
    return render(request, template, context)