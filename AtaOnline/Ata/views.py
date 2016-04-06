"""Django views."""
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.template import RequestContext

# Create your views here.


class Index(View):
    """Home page for AtaOnline."""

    def get(self, request):
        """Index."""
        if request.user.is_authenticated():
            respond_view = redirect('home')
        else:
            respond_view = render_to_response(
                'login.html', context_instance=RequestContext(request))
        return respond_view


class Login(View):
    """This class will define every method that has login in."""

    http_method_names = [u'get', u'post']

    def post(self, request):
        """Loggin method."""
        request_username = request.POST.get('username')
        request_password = request.POST.get('password')

        user = authenticate(username=request_username,
                            password=request_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                respond_view = redirect('/home/')
            else:
                respond_view = render_to_response('UserOff.html')
        else:
            respond_view = render_to_response('UserIsNone.html')

        return respond_view
