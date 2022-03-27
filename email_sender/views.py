from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import json
import re

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

def detect(text, regex="Rs\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?"):
    amount = re.findall(regex, text)
    processed_data = {"status":"ok", "count": len(amount), "amount":amount}
    json_object = json.dumps(processed_data, indent=4)
    return json_object


@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        send_email(username=data['username'], send_to=data['send_to'])
        return HttpResponse("Email Sent")
    return HttpResponse("Please send POST request")


def server_info(request):
    if request.method == "GET":
        return HttpResponse("Amount Detector\nRunning on Heroku")

@csrf_exempt
def server_detect(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'text' and 'regex' in data:
            result = detect(text=data['text'], regex=data['regex'])
            return HttpResponse(result)
        elif 'text' in data:
            result = detect(text=data['text'])
            return HttpResponse(result)
        else:
            return HttpResponse("Please send text and optionally regex pattern to process")
    else:
        return HttpResponse("Please send POST request")