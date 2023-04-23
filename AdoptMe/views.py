from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AdoptMe.models import Post, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, "AdoptMe/about.html")

def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "AdoptMe/index.html", context)

class PostList(ListView):
    model = Post
    context_object_name = "posts"
    
class PostDetail(DetailView):
    model = Post
    
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = ['nombre_carousel','caracteristicas_carousel',
            'nombre','caracteristicas','imagen']


    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super().form_valid(form)
     

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = ['nombre_carousel','caracteristicas_carousel',
            'nombre','caracteristicas','imagen']

    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(editor=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "AdoptMe/not_found.html")

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(editor=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "AdoptMe/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = 'registration/logout.html'


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = '__all__'

   
    

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "AdoptMe/not_found.html")

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy("mensaje-create")


class  MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()
    

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()
