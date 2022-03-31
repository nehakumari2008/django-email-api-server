from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import json
import re

from .models import MyRegex

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

def get_all_regex(request):
    regexs = MyRegex.objects.all()
    regex_list = []
    for item in regexs:
        regex_list.append({'id': item.id, 'label': item.label, 'regex': item.regex })
    json_data = json.dumps(regex_list)
    return HttpResponse(json_data)


@csrf_exempt
def regex_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'regex' and 'label' in data:
            regex = data['regex']
            label = data['label']
            myregex =MyRegex(regex=regex, label=label)
            myregex.save()
            return HttpResponse("Regex save successfully")

def regex_delete(request, item_id):
    regex = get_object_or_404(MyRegex, pk=item_id)
    regex.delete()
    return HttpResponse("Regex deleted")

def get_regex(request, item_id):
    regex = get_object_or_404(MyRegex, pk=item_id)
    data = {'id':regex.id, 'label':regex.label, 'regex':regex.regex}
    json_data = json.dumps(data)
    return HttpResponse(json_data)

@csrf_exempt
def edit_regex(request, item_id):
    data_to_edit = get_object_or_404(MyRegex, pk=item_id)
    if request.method == "POST":
        data = json.loads(request.body)
        regex = data['regex']
        label = data['label']
        data_to_edit.regex = regex
        data_to_edit.label = label
        data_to_edit.save()
        return HttpResponse("Regex Edited")

def regex_search(request, query):
    results = MyRegex.objects.all().filter(regex__startswith=query)
    result_data = []
    for item in results:
        result_data.append({'id': item.id, 'label': item.label, 'regex': item.regex})
    json_data = json.dumps(result_data)
    return HttpResponse(json_data)
