from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Authors, Posts


def my_view(request):
    context = {"name": "Den"}
    return render(request, "lesson3/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "lesson3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый'
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'lesson3/templ_for.html', context)


def index(request):
    return render(request, 'lesson3/index.html')


def about(request):
    return render(request, 'lesson3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Authors, pk=author_id)
    posts = Posts.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'lesson3/author_posts.html', {'author': author,'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'lesson3/post_full.html', {'post': post})
