from django.shortcuts import render, redirect
from .models import Post
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, PostForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse

# Create your views here.
# Home View
#Using class based views
class PostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'posts'
    ordering = ["-time_posted"]
    paginate_by = 6

#Detail View
class PostDetailView(DetailView):
    model = Post
    template_name = "single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        related_posts = Post.objects.filter(post_category__in=post.post_category.all()).exclude(id=post.id).distinct()[:5]
        context['related_posts'] = related_posts
        return context
         
# Create View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "user_home.html"
    login_url = 'login'
    

    def form_valid(self, form):
        form.instance.author = self.request.user  # Associate the post with the current user
        return super().form_valid(form)


#Update View
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "user_home.html"
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_object(self, queryset = None):
        return Post.objects.get(id=self.kwargs['pk'])

    
#Delete View
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = '/dev-blog/user-blog'

#About View
def about(request):
    return render(request, 'about.html')

#Contact View
def contact(request):
    return render(request, 'contact.html')

#Users Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


#User Blog view
@login_required
def user_blog(request):
    posts = Post.objects.filter(author=request.user)

    context = {'posts':posts}
    return render(request, 'personal_blog.html', context)

#Register View
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, "Your password can’t be too similar to your other personal information, Your password must contain at least 8 characters, Your password can’t be a commonly used password, Your password can’t be entirely numeric.")
            return render(request, 'register.html', {'form':form})
    else:
        form = UserRegistrationForm()

    context = {'form':form}
    return render(request, 'register.html', context)

#Search View
def search(request):
    query = request.GET.get('query', '')
    results = []
    
    if query:
        # Filter the `Post` model based on the query.
        results = Post.objects.filter(title__contains=query) | Post.objects.filter(description__contains=query)
    
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'index.html', context)
