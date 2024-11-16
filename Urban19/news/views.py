from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
def post_list(request):
    # получаем все посты
    posts = Post.objects.all().order_by('created_at')

    # создаем пагинатор
    posts_per_page = request.GET.get("posts_per_page")
    if posts_per_page:
        paginator = Paginator(posts, posts_per_page)
    else:
        paginator = Paginator(posts, 5)  # 5 постов на странице
        posts_per_page = 5


    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(
        request,
        'post_list.html',
        {'page_posts': page_posts, 'paginator': paginator, 'posts_per_page': posts_per_page}
    )
