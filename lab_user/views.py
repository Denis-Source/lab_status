from rest_framework.generics import RetrieveAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from lab_user.models import LabUser
from lab_user.serializers import LabUserSerializer, LabUserConfidentialSerializer
from lab_user.forms import RegisterForm, LoginForm, ProfileUpdateForm


class LabUserRetrieveAPIView(RetrieveAPIView):
    serializer_class = LabUserSerializer

    queryset = LabUser.objects.all()

    lookup_field = "username"


class LabUserConfidentialRetrieveAPIView(LabUserRetrieveAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LabUserConfidentialSerializer


class RegisterView(FormView):
    """
    User registration form view
    Uses a django builtin User model

    After a successful form validation
    logs a newly registered user in
    redirects to the main page
    """
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        """
        Form validation Override method
        If form is valid
        Saves a newly registered user
        Uses it's parameters (username and password1) to login the user
        :param form:
        :return:
        """
        form.save()

        # logs user
        user = authenticate(
            username=self.request.POST["username"],
            password=self.request.POST["password1"]
        )
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    """
    User login form view
    Uses a django User mode

    After a successful login
    redirects user to the main page
    """
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        """
        Form valid method
        :param form:
        :return:
        """
        super(LoginView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        Logs an user in
        Else redirects back to the login page
        Sends a corresponding message
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        messages.error(request, "Wrong login or password")
        return redirect("/login/")

    @staticmethod
    def logout_view(request):
        """
        Log out view
        Redirects to the login page
        :param request:
        :return:
        """
        logout(request)
        return redirect("/login/")