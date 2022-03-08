from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        message_name = request.POST.get('name')
       # message_email = request.POST.get('message-email')
        message = request.POST.get('message')
        send_mail(
            
            message,
            message_name,
            'shanksfk@gmail.com',
            ['mfbk93@gmail.com'])

        return render(request,'contact.html', {'message_name':message_name})

    else:
        return render(request,'index.html',{})
    
def contact(request):
    if request.method == 'POST':
        message_name = request.POST('name')
        message_email = request.POST('message-email')
        message = request.POST('message')
        send_mail(
            
            message,
            message_name,
            'shanksfk@gmail.com',
            ['mfbk93@gmail.com'])

        return render(request,'contact.html', {'message_name':message_name})

    else:
        return render(request,'index.html',{})

