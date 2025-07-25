from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 글부터 정렬
    return render(request, 'freeboard/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('freeboard_post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'freeboard/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })
