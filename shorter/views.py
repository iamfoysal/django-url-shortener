from django.shortcuts import render, redirect
from .models import Url
import random
import string
from django.utils import timezone
from django.urls import reverse
import requests

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(7))


def get_country_from_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        print(response)
        data = response.json()
        country = data.get('country', '')
        return country
    except Exception as e:
        print(f"Error getting country: {e}")
        return ''



def index(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = generate_short_code()
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
        print("User IP: ",user_ip)
        country = get_country_from_ip(user_ip)
        
        url_obj, created = Url.objects.get_or_create(original_url=original_url, short_code=short_code, user=request.user, location=country)
        # return render(request, 'shorter/shorted.html', {'url_obj': url_obj})
        return redirect(reverse('shorter:shorted', kwargs={'short_code': url_obj.short_code}))

    return render(request, 'shorter/index.html')

def redirect_original(request, short_code):
    try:
        print("Short code: ", short_code)
        url_obj = Url.objects.get(short_code=short_code)
        url_obj.clicks += 1
        url_obj.last_click = timezone.now()
        url_obj.save()
        return redirect(url_obj.original_url)
    except Exception as e:
        print(f"Error getting URL: {e}")
        return redirect(reverse('shorter:index'))


def list_urls(request):
    url_objs = Url.objects.filter(user=request.user)
    return render(request, 'shorter/list.html', {'url_objs': url_objs})

def shorted(request, short_code):
    url_obj = Url.objects.get(short_code=short_code)
    return render(request, 'shorter/shorted.html', {'url_obj': url_obj})