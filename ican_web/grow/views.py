from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied #포스트 작성자만 수정 가능

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'diary/post_list.html'
    paginate_by = 9

class PostDetail(DetailView):
    model = Post

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'detail', 'image', 'file_upload']
    template_name = 'grow/post_update_form.html'  # 특정한 템플릿명 지정 가능

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:  # user==author면 수정 가능하다는 의미
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied