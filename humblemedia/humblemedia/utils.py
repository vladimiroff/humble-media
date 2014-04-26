from django.contrib.auth.decorators import login_required


class LoginRequiredMixin:
    @classmethod
    def as_view(cls, *args, **kwargs):
        res = super().as_view(*args, **kwargs)
        return login_required(res)
