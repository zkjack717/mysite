from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from .models import Blog, BlogType
from read_statistics.utils import read_statistics_ones_read


# Create your views here.


def blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # each
    page_num = request.GET.get('page', 1)  # get page
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  # get current page
    page_range = [i for i in range(current_page_num - 2, current_page_num + 3) if 1 < i < paginator.num_pages]
    page_range.insert(0, 1)
    if current_page_num >= 4:
        page_range.insert(1, '...')
    if current_page_num <= paginator.num_pages - 4:
        page_range.append('...')
    if paginator.num_pages != 1:
        page_range.append(paginator.num_pages)
    '''
    # 获取博客分类的对应博客数量
    BlogType.objects.annotate(blog_count=Count('blog'))
    blog_types = BlogType.objects.all()
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)
    '''
    
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {'blogs': page_of_blogs.object_list,
               'page_of_blogs': page_of_blogs,
               'page_range': page_range,
               'blog_count': Blog.objects.all().count(),
               'blog_types': BlogType.objects.annotate(blog_count=Count('blog')),
               'blog_dates': blog_dates_dict,
               }
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = blog_list_common_data(request, blogs_all_list)
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, id=blog_pk)
    read_cookie_key = read_statistics_ones_read(request, blog)

    context = {'blog': blog,
               'previous_blog': Blog.objects.filter(created_time__gt=blog.created_time).last(),
               'next_blog': Blog.objects.filter(created_time__lt=blog.created_time).first(),
               }
    response = render(request, 'blog/blog_detail.html', context)
    response.set_cookie(read_cookie_key, 'true')
    return response


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blogs_with_type.html', context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s-%s' % (year, month)
    return render(request, 'blog/blogs_with_date.html', context)
