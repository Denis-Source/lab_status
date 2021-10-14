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
