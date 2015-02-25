from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home')
def home_view(request):
    return Response('Hello World')

@view_config(route_name='hello')
def hello_world_view(request):
    return Response('Hello %(name)s' % (request.matchdict))
