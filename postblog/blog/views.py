
from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home_view(request):

    all_posts = Post.objects.all()
    # Create a Paginator object with a specific number of items per page
    paginator = Paginator(all_posts, 3  )  # Show 10 posts per page (you can change this number)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, display the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, display the last page
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/homepage.html', context)




def blog(request, id):

    posts = Post.objects.filter(id=id)

    context= {
        "posts": posts
    }

    return render(request, 'blog/blog.html', context)


def about_view(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'blog/blog.html', {'post': post, 'form': form})


