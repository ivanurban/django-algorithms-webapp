from django.urls import path
from . import views


app_name = 'algoblog'


urlpatterns = [
# post views
    path('', views.AlgoBlogListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', views.AlgoBlogDetailView.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(),name='contact'),


    #path('<slug:post>/', views.AlgoBlogDetailView.as_view(), name='post_detail'),

]