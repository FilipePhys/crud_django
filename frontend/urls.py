from django.urls import path, include
from .views import SignUpView, HomePageView, ProfileView, ProfileChangeView, ProfileDeleteView

urlpatterns = [
    path(r'profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profiledelete'),
    path(r'profile/<int:pk>/changes/', ProfileChangeView.as_view(), name='profilechange'),
    path(r'profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', include('django.contrib.auth.urls')),  # new
    path('', HomePageView.as_view(), name='home'),
]

