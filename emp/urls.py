from django.urls import path
from . import views
urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='register-view'),
  path('login/', views.LoginView.as_view(), name='login-view'),
  path('logout/', views.LogoutView.as_view(), name='logout-view'),
  path('dashboard/', views.UserDashboard, name='dashboard-view'),

  path('user-details/<int:id>', views.user_details, name='user-details'),
  path('user-update/<int:id>', views.users_update, name='user-update'),
  path('user-delete/<int:id>', views.user_delete, name='user-delete'),
]