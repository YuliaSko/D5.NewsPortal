from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import RegisterForm
from news.models import Author


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = '/'


@login_required()
def im_author(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)

    if not Author.objects.filter(user=user).exists():
        Author.objects.create(user=user)
    return redirect('/')
