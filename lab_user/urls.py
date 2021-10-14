from django.urls import path

from lab_user.views import RegisterView, LoginView


urlpatterns = [
    # registration form path
    path("register/", RegisterView.as_view()),

    # login form path
    path("login/", LoginView.as_view()),

    # logout path
    path("logout/", LoginView.logout_view),

    # profile path
    # path("profile/", ProfileView.as_view()),
    # generate token
    # path("profile/generate-token", ProfileView.generate_token_view)
]
