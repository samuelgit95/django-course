from django.shortcuts import render

# Create your views here.
def register_user(request):
    return render(request, 'users/register_user.html')