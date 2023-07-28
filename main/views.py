from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Link

def render_links(request):
    if request.method == "POST":
        #using requests lib, import/get the webpage we desire to scrape data from
        web_page = requests.get(request.POST.get('site', ''))
        # now using Beautiful Soup, we get all the html code in the web_page obj
        # returned by requests lib
        html_content = BeautifulSoup(web_page.text, 'html.parser')

        # we get all anchor tags and retrieve links and store in links list
    
        for anchor_tags in html_content.find_all('a'):
            link_name = anchor_tags.string  #using string we can get the name of the link
            link_address = anchor_tags.get('href')
            Link.objects.create(name = link_name, address = link_address).save()

        return HttpResponseRedirect(redirect_to='scrape')
    else:
        links = Link.objects.all()

    return render(request, 'main/links.html', context= {'links': links})

def delete_links(request):
    Link.objects.all().delete()
    return render(request, 'main/links.html')

