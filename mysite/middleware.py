from books.models import AuthRequest


class SaveAuthenticationRequestMiddleware(object):

    def process_request(self, request):
        if request.method == 'POST':
            auth_req = AuthRequest(
               username = request.POST.__getitem__('username'),
               password = request.POST.__getitem__('password'))
            auth_req.save()
