from django.http import HttpResponse
from django.shortcuts import render
from details.models import Dynamic
from testapp.models import House
from contactform.models import Contactform
from django.core.mail import send_mail
import requests
import os
import xml.etree.ElementTree as ET
from django.conf import settings

def HomePage(request):
    serviceData = Dynamic.objects.all()
    data = {
        'serviceData': serviceData
    }
    return render(request, "index.html", data)

def ContactPage(request):
    msg = ""
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if fullname == "" or email == "" or message == "" or subject == "":
            msg = "All fields are required"
        else:
            alldata = Contactform(fullname=fullname, email=email, subject=subject, message=message)
            alldata.save()
            msg = "Data inserted"
            subject = 'Test Email'
            message = 'This is a test email.'
            from_email = 'kumkumsharma25004@gmail.com'
            recipient_list = ['kumkumsharma25004@gmail.com']
            send_mail(subject, message, from_email, recipient_list)

    return render(request, "contact.html", {'msg': msg})

def countriesData(request):
    api_url = "https://api.first.org/data/v1/countries"
    response = requests.get(api_url)
    if response.status_code == 200:
        countries_data = response.json()
        countries = countries_data.get('data', {})
    else:
        countries = {}

    return render(request, 'print_json.html', {'countries': countries})
def read_xml(request):
    # Path to the XML file
    # Path to the XML file
    xml_path = os.path.join("static", "xml", "countries.xml")
    
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract data (Assuming a structure like <Country><Name>...</Name></Country>)
    countries = []
    for country in root.findall("Country"):  # Adjust 'Country' based on your XML structure
            name = country.find("Name").text if country.find("Name") is not None else "Unknown"
            code = country.find("Code").text if country.find("Code") is not None else "N/A"
            countries.append({"name": name, "code": code})
    # Pass the data to the template
    return render(request, 'print_xml.html', {'countries': countries})
    

def house_rooms(request):
    house = House.objects.get(id=1)
    rooms = house.my.all()
    return render(request, 'house_room.html', {'house': house, 'rooms': rooms})

