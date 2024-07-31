from django.urls import path

from accounts import views

app_name = "acounts"
urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path('logout/', views.user_logout_view, name="logout"),
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('register/code/', views.UserVerificationcodeView.as_view(), name="Verificationcode"),
    path('editprofile/', views.UserEditView.as_view(), name="edit_user"),
    path("deleteuser/",views.delete_user_view,name="delete_user"),
    path("", views.UserEditProfileView.as_view(), name="edit_profile_user")
]
