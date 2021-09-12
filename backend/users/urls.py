from django.urls import path
from users.views import RegistrationView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', views.logout),
    path('register/', RegistrationView.as_view(), name='register')
]
