from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('signup/', views.signup, name='signup'),
path('dealer/<int:pk>/', views.dealer_detail, name='dealer_detail'),
path('dealer/<int:pk>/add_review/', views.add_review, name='add_review'),
]