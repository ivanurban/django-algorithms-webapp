from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView, FormView

from .forms import ContactForm

from .models import Post

from django.urls import reverse_lazy



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

# class ContactView(TemplateView):
#     template_name = 'algoblog/post/contact.html'    

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'algoblog/post/contact.html'    
    success_url = reverse_lazy('algoblog:success')


    def form_valid(self, form):
        #calls custom send method from forms.py
        form.send()
        return super().form_valid(form)


# contact/views.py
class ContactSuccessView(TemplateView):
    template_name = 'algoblog/post/success.html'





