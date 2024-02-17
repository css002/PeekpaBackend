from django.urls import path

from apps.api.view_auth import LoginView,LoginAdminView,RegisterUserView,UserAdminView
from apps.api.view_job import ResumeView,AvatarView

app_name = "api"

urlpatterns = [
    path("auth/signin/", LoginView.as_view(), name='signin_view'),
    path("auth/signup/", RegisterUserView.as_view(), name="signup"),
    path("auth/login/", LoginAdminView.as_view(), name="login_admin"),
    path("manage/user/", UserAdminView.as_view(), name="user_admin"),
    path("resume/upload/", ResumeView.as_view(), name='resume_upload'),
    path("avatar/upload/", AvatarView.as_view(), name='avatar_upload'),
]