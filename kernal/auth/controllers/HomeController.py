''' A Module Description '''
from app.http.providers.view import view
from config import application
from packages.facades.Auth import Auth

class HomeController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, request):
        if not Auth(request).user():
            request.redirect('/login')
        return view('auth/home', {'app': application, 'Auth': Auth(request)})
