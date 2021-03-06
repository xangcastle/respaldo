import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseForbidden, \
HttpResponseBadRequest
from django.views.generic import View
from django.core import serializers
from metropolitana.models import Paquete, Tipificacion
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

try:
    # Django 1.5 and higher supports overriding the default User model
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User

    def get_user_model():
        """
        Return the default User class (for Django < 1.5
        :return:
        """
        return User


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, response_class=HttpResponse):
        """
        Render the context to json
        :param context:
        :param response_class: Defaults to regular HttpResponse
        :return:
        """
        return self.get_json_response(self.convert_context_to_json(context), response_class)

    def get_json_response(self, content, response_class, **httpresponse_kwargs):
        """
        Create the response object and set the response header
        :param content:
        :param response_class:
        :param httpresponse_kwargs:
        :return:
        """
        return response_class(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        """
        Convert the content to json
        :param context:
        :return:
        """
        return json.dumps(context)


class LoginView(JSONResponseMixin, View):
    """
    The login view class. This will attempt to authenticate the user
    and will send a response object with the status/error message.
    """

    def post(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        context = {}
        username = self.request.POST.get('username', '')
        password = self.request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                context['success'] = True
                return self.render_to_json_response(context)
            else:
                # Return a 'disabled account' error message
                context['success'] = False
                context['error_msg'] = 'User account has been disabled.'
        else:
            # Return an 'invalid login' error message.
            context['success'] = False
            context['error_msg'] = 'Invalid username/password.'

        return self.render_to_json_response(context, HttpResponseForbidden)


class LogoutView(JSONResponseMixin, View):
    """
    The logout view class. This will log the user out and invalidate the session.
    """

    def post(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        logout(self.request)
        return self.render_to_json_response({'success': True})


class RegisterView(JSONResponseMixin, View):
    """
    The register view class. This will attempt to create a user from the
    supplied username and password.
    If the username already exists, a 400 response is sent back
    """

    def post(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        context = {}
        username = self.request.POST['username']
        password = self.request.POST['password']
        password_confirm = self.request.POST['password_confirm']

        if password != password_confirm:
            context['success'] = False
            context['error_msg'] = 'Password does not match the confirm password.'
            return self.render_to_json_response(context, HttpResponseBadRequest)

        try:
            user = get_user_model().objects.create_user(username, password=password)
            user = authenticate(username=username, password=password)
            login(self.request, user)
            context['success'] = True
            return self.render_to_json_response(context)
        except IntegrityError:
            # Return an 'invalid user' error message.
            context['success'] = False
            context['error_msg'] = 'User already exists.'
            return self.render_to_json_response(context, HttpResponseBadRequest)


class TestPageView(TemplateView):
    template_name = "test.html"


@csrf_exempt
def get_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user:
        data = serializers.serialize('json', [user, ])
        struct = json.loads(data)
        data = json.dumps(struct[0])
    else:
        data = None
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def get_paquetes(request):
    ciclo = request.POST.get('ciclo', '')
    mes = request.POST.get('mes', '')
    queryset = Paquete.objects.filter(ciclo=ciclo, mes=mes)
    if queryset:
        data = serializers.serialize('json', queryset)
        struct = json.loads(data)
        data = json.dumps(struct)
    else:
        data = None
    return HttpResponse(data, content_type='application/json')


def get_paquete(request):
    obj_json = {}
    obj_json['Usuario'] = request.POST.get('Usuario')
    obj_json['Motivo'] = request.POST.get('Motivo')
    obj_json['Barra'] = request.POST.get('Barra')
    obj_json['Fecha'] = request.POST.get('Fecha')
    obj_json['Parentezco'] = request.POST.get('Parentezco')
    obj_json['Recibe'] = request.POST.get('Recibe')
    obj_json['Imagen'] = request.POST.get('Imagen')
    obj_json['Mensaje'] = ''
    try:
        u = User.objects.get(username=obj_json['Usuario'])
    except:
        u = None
    try:
        t = Tipificacion.objects.get(id=int(obj_json['Motivo']))
    except:
        t = None
    try:
        p = Paquete.objects.get(barra=obj_json['Barra'])
    except:
        p = None
    if p:
        if p.imagen:
            obj_json['Mensaje'] = "Este paquete ya fue cargado"
        else:
            p.user = u
            p.tipificacion = t
            p.fecha_entrega = obj_json['Fecha']
            p.parentezco = obj_json['Parentezco']
            p.recibe = obj_json['Recibe']
            p.imagen = obj_json['Imagen']
            obj_json['Mensaje'] = "Paquete cargado Correctamente"
            p.save()
    data = json.dumps(obj_json)
    return HttpResponse(data, content_type='application/json')