from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, Http404
from django.views.generic import DetailView

User = get_user_model()


class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
