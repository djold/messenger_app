from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.models import User
from .models import SubscribeModel

# Create your views here.

def subscribe_view(request, pk):
    if request.method == 'POST':
        self_user = request.user
        other_user = get_object_or_404(User, pk=pk)
        if self_user != other_user and not SubscribeModel.objects.filter(self_user=self_user, other_user=other_user).exists():
            s_model = SubscribeModel(self_user=self_user, other_user=other_user)
            s_model.save()
    return redirect("/")






