from django.urls import path
from users.views import RegistrationStudentUserView

urlpatterns = [
    # path('login/', views.login),
    # path('logout/', views.logout),
    path('register/', RegistrationStudentUserView.as_view())
]
