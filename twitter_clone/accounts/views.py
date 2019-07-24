from django.shortcuts import render,redirect
from tweets.models import Tweet
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# def login_view(request):
#     if request.user.is_authenticated:
#         # message = 'ur already logined'
#         return redirect('tweets:tweet_list')

#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             new_user = authenticate(request, username=cd['username'], password=cd['password'])
#             if new_user is not None:
#                 if new_user.is_active:
#                     login(request, new_user)
#                     return redirect('tweets:tweet_list')
#                 else:
#                     return HttpResponse('ur not active')
#             else:
#                 return HttpResponse('username and password didn\'t match')
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return redirect('accounts:login')
