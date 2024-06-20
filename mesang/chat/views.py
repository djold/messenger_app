from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ChatModel
from .forms import ChatForm

# Create your views here.

def index_view(request):
    form = ChatForm(request.POST or None)
    chat = ChatModel.objects.all()
    return render(request, 'index.html', {'form': form, 'chat': chat})


@login_required(login_url='/login/')
def send_view(request):
    if request.POST:
        form = ChatForm(request.POST)
        if form.is_valid():
            user = request.user
            text = form.cleaned_data.get('text')
            chat_model = ChatModel(user=user, text=text)
            chat_model.save()
    return HttpResponseRedirect(reverse('index'))






