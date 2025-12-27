from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Contact
from ourguardsnew.models import Ourguards
from aboutus.models import Aboutus
from aboutus2.models import Aboutus2
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
import requests


def index_page(request):
    return render(request, "index.html")


def about_page(request):
    # serviceData = Service.objects.all()
    aboutData = Aboutus.objects.all()
    aboutData2 = Aboutus2.objects.all()
    data = {
        # 'serviceData': serviceData,
        'aboutData': aboutData,
        'aboutData2': aboutData2
    }
    return render(request, "about.html", data)


def story_page(request):
    return render(request, "story.html")


def gallery_page(request):
    OurguardData = Ourguards.objects.all()
    data = {
        'ourguardData': OurguardData
    }
    return render(request, "gallery.html", data)


def contact_page(request):
    msg = ''
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        no_of_guests = request.POST.get('no_of_guests')
        message = request.POST.get('message')

        # Save contact form data
        allcontact = Contact(
            firstname=firstname,
            lastname=lastname,
            email=email,
            no_of_guests=no_of_guests,
            phone=phone,
            message=message
        )
        allcontact.save()

        msg = 'Your response has been recorded. Thank you!'

        # Email content
        subjects = f"Thank You for Contacting Us - for Wedding Enquiry"
        html_content = render_to_string('email_template.html',{
            'firstname':firstname,
            'lastname':lastname,
            'message':message,
            'email':email,
            'no_of_guests':no_of_guests
            })
        text_content = (
          f"Dear {firstname},{lastname}\n\n"
          "Thank you for contacting Sangam University. Wehave received your message and will get back to you soon.\n\n"
 "Best regards,\nSangam University Support Team"
 )
      

        
    
        # Send html email to the user
        emails =EmailMultiAlternatives(
            subject=subjects,
            body=text_content,
            from_email="komalvai7@gmail.com",
            to=[email],
        )
        
        emails.attach_alternative(html_content, "text/html")
        emails.send(fail_silently=False)

        # Send a copy to the admin
        admin_subject = f"New Contact Form Submission from {firstname}{lastname}"
        admin_message = (
            f"New message received from contact form:\n\n"
            f"Firstname: {firstname}\n"
            f"Lastname: {lastname}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"No_of_guests: {no_of_guests}\n"
            f"Message:\n{message}\n"
        )
       
        admin_email = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_message,
            from_email="komalvai7@gmail.com",
            to=["vaishnavkomal60@gmail.com"],
        )
        admin_email.send(
            fail_silently=False,
    
        )
        

    return render(request, "contact.html", {'msg': msg})

def wedding_venues(request):
    api_url = "https://raw.githubusercontent.com/Komalvaishnav-007/JSON-Server-API/main/db.json"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # venues = data.get('venues', [])  # if nested under 'venues' key
            venues = data  # Direct array as per your sample
        else:
            venues = []
    except:
        venues = []
    return render(request, 'print_json.html', {'venues': venues})

