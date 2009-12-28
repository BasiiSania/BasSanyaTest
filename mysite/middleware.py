from books.models import AuthRequest


class SaveAuthenticationRequestMiddleware(object):

    def process_request(self, request):
        if request.method == 'POST' and request.path == r'^accounts/login/$':
            auth_req = AuthRequest(
               enter_login = request.POST.__getitem__('username'),
               enter_pass = request.POST.__getitem__('password'))
            auth_req.save()
