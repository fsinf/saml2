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
        changed = False
        if user.email is None or user.email == '':
            user.email = f"{username_lower}@fsinf.at"
            changed = True
        if user.first_name is None or user.first_name == '':
            user.first_name = f"{username_lower}"
            changed = True
        if user.last_name is None or user.last_name == '':
            user.last_name = "-"
            changed = True
        if changed:
            user.save()
        user_email = user.email
        return user
