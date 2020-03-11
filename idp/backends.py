#    'django_pam.auth.backends.PAMBackend',
from django_pam.auth.backends import PAMBackend

class PAMRestAuthBackend(PAMBackend):
    def authenticate(self, *args, **kwargs):
        kwargs.pop('service', None)
        return super().authenticate(*args, service='saml2', **kwargs)
