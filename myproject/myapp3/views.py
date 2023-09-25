from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from .models import Author, Post
from django.shortcuts import render, get_object_or_404




def hello(request):
    return HttpResponse('Hello World from function!')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello World from class!')


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(F"Post from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за месяц и год
        return HttpResponse(F"Post from {year}/{month}<br>{text}")


def post_detail(request, year, month, slug):
    ...  # TODO:
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создает списки в питон лист или []",
        "content": "D klnoh;kjh;kjh lkjhj;kjkjbh ljkk;jk;jhk kghhg"
                   "hjvjhvvjhvjvjvjgvgjvjgvgvjgvb jhgjvjv"

    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Привет мир!"
        context['number'] = 5
        return context


# Create your views here.

def view_for(request):
    my_list = ['apple', 'orange', 'banana', ]
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'желтый',
        'знать': 'зеленый',
        'где': 'голубой',
        'сидит': ' синий',
        'фазан': 'фиoлетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)

def index(request):
    return render(request, 'myapp3/index.html')

def about(request):
    return render(request,'myapp3/about.html')

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})

