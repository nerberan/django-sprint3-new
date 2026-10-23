from django.shortcuts import render, get_object_or_404
from .models import Post, Category


POSTS_LIMIT = 5


def index(request):
    template_name = 'blog/index.html'

    post_list = (
        Post.objects.published()
        .select_related('category')
        [:POSTS_LIMIT]
    )

    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects.published().select_related('category'), pk=id)

    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.published().filter(
        category__slug=category_slug
    ).select_related('category')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)


"""
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


POSTS_LIMIT = 5


def index(request):
    template_name = 'blog/index.html'

    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related('category').order_by('-pub_date')[:POSTS_LIMIT]

    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ).select_related('category'),
        pk=id
    )

    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('category').order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)
    """
