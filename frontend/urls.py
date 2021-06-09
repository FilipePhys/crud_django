from django.urls import path, include
from .views import SignUpView, HomePageView, ProfileView, ProfileChangeView

urlpatterns = [
    path(r'profile/<int:pk>/changes/', ProfileChangeView.as_view(), name='profilechange'),
    path(r'profile/<int:pk>', ProfileView.as_view(), name='profile'),
    #path('teste/', test_view, name='tiopablo'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', include('django.contrib.auth.urls')),  # new
    path('', HomePageView.as_view(), name='home'),
]

