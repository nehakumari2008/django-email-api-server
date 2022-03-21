from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import json

def send_email(username, send_to):
    msg = EmailMessage(
        from_email='neharoberts32@gmail.com',
        to=[send_to],
    )
    msg.template_id = "d-9c5c3e1cd3964476ad4b18f997683acb"
    msg.dynamic_template_data = {
        "username": username
    }
    msg.send(fail_silently=False)


@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        send_email(username=data['username'], send_to=data['send_to'])

    return HttpResponse(request.method)
