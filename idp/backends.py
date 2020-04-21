#    'django_pam.auth.backends.PAMBackend',
from django_pam.auth.backends import PAMBackend

class PAMRestAuthBackend(PAMBackend):
    def authenticate(self, *args, **kwargs):
        service = kwargs.pop('service', None)
        username = kwargs.pop('username', None)
        password = kwargs.pop('password', None)
        extra_fields = kwargs.pop('extra_fields', None)
        if username is None or password is None:
            return None
        username_lower = username.lower()
        if extra_fields is not None:
            user = super().authenticate(*args, service='saml2', username=username_lower, password=password, extra_fields=extra_fields)
        else:
            user = super().authenticate(*args, service='saml2', username=username_lower, password=password)
        if user is None:
            return None
        if user.email is None or user.email == '':
            user.email = f"{username_lower}@fsinf.at"
            user.save()
        user_email = user.email
        return user
