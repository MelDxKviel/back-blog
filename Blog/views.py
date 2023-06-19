from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.utils.text import slugify

from .models import Post, Comment, Category, Tag
from .forms import PostCreateForm, CommentForm, CategoryCreateForm, TagCreateForm
from .utils import spam_check


class PostListView(generic.ListView):
    queryset = Post.objects.order_by('-created_at')
    paginate_by = 3
    template_name = 'Blog/post_list.html'


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    template_name = 'Blog/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return f'/posts/{self.get_object().slug}'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('You are not authenticated')
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = self.get_object()
        if spam_check(form.cleaned_data['text']):
            comment = Comment.objects.create(
                text=form.cleaned_data['text'],
                author=self.request.user,
                post=self.get_object(),
            )
            return super(PostDetailView, self).form_valid(form)
        else:
            messages.error(self.request, 'Your comment is a spam')
            return self.render_to_response(self.get_context_data(form=form))


class PostCreateView(LoginRequiredMixin, generic.FormView):
    model = Post
    login_url = '/login/'
    form_class = PostCreateForm
    template_name = 'Blog/post_create.html'
    success_url = '/posts'

    def form_valid(self, form):
        post = Post.objects.create(
            title=form.cleaned_data['title'],
            slug=slugify(form.cleaned_data['title']),
            content=form.cleaned_data['content'],
            category=form.cleaned_data['category'],
            author=self.request.user,
        )
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    login_url = '/login/'
    form = PostCreateForm
    template_name = 'Blog/post_update.html'
    fields = ['title', 'content', 'category', 'tags', ]

    def get_success_url(self):
        return f'/posts/{self.get_object().slug}'

    def get(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Cannot edit other's posts")

    def post(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Cannot edit other's posts")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = '/posts'

    def get(self, request, *args, **kwargs):
        return HttpResponseForbidden("Cannot delete via GET")

    def delete(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Cannot delete other's post")


class CommentDelete(LoginRequiredMixin, generic.DeleteView):
    model = Comment

    def get_success_url(self):
        return f'/posts/{self.get_object().post.slug}'

    def delete(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Cannot delete other's comments")


class CategoryListView(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'Blog/category_list.html'


class CategoryCreateView(LoginRequiredMixin, generic.FormView):
    model = Category
    login_url = '/login/'
    form_class = CategoryCreateForm
    template_name = 'Blog/category_create.html'
    success_url = '/posts'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Only admins can add category")

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Only admins can add category")

    def form_valid(self, form):
        category = Category.objects.create(
            category_name=form.cleaned_data['category_name'],
        )
        return super(CategoryCreateView, self).form_valid(form)


class CategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Category

    def get_success_url(self):
        return '/categories'

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Only admins can delete categories")


class TagCreateView(LoginRequiredMixin, generic.FormView):
    model = Tag
    login_url = '/login/'
    form_class = TagCreateForm
    template_name = 'Blog/tag_create.html'
    success_url = '/posts'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Only admins can add tags")

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Only admins can add tags")

    def form_valid(self, form):
        tag = Tag.objects.create(
            tag_name=form.cleaned_data['tag_name'],
        )
        return super(TagCreateView, self).form_valid(form)
