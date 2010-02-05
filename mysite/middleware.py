from mydata.models import AuthRequest


class SaveAuthenticationRequestMiddleware(object):

    def process_request(self, request):
        if request.method == 'POST' and request.path == '/accounts/login/':
            try:
                auth_req = AuthRequest(
                   enter_login = request.POST['username'],
                   enter_pass = request.POST['password'])
                auth_req.save()
            except KeyError:
                print "POST['username'] or POST['password'] is not exist"
