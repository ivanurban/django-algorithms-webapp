from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView

from .models import Post



# Create your views here.

class AlgoBlogListView(ListView):
    model = Post 

    template_name = 'algoblog/post/list.html' 
    def get_context_data(self, **kwargs):
        context = super(AlgoBlogListView, self).get_context_data(**kwargs)
        context['latest_algorithm'] = Post.objects.all()[:1]
        return context 

class AlgoBlogDetailView(DetailView):
    model = Post
    # slug_field = 'slug'
    # slug_url_kwarg = 'slug'
    template_name = 'algoblog/post/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(AlgoBlogDetailView, self).get_context_data(*args, **kwargs)
        context['link_list'] = Post.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'algoblog/post/about.html'    

class ContactView(TemplateView):
    template_name = 'algoblog/post/contact.html'    


