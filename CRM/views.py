from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo
from CRM.models import UserInfo

def IndexPage(request):
    return render(request,"index.html")

def LoginPage(request):
    if request.method == 'POST':
        membership_id = request.POST.get('membership_id')
        passw = request.POST.get('passw')
        try:
            user_info = UserInfo.objects.get(membership_id=membership_id)
            context = {
                'fname': user_info.fname,
                'lname': user_info.lname,
                'membership_id': user_info.membership_id,
            }
            return render(request, 'Dash.html', context)
        except UserInfo.DoesNotExist:
            return render(request, 'Dash.html', {'error_message': 'User not found'})
    
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'Dash1.html')