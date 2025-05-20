from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, LoginForm , AddContact
from .models import Audience, Contact

def home_view(request):
    return render(request, 'emailtool/home.html')
# Homepage (Landing page)
@login_required
def index(request):
    return render(request, 'emailtool/index.html')

# Home view (Dashboard welcome screen)



# Audience Dashboard
@login_required
def audience_dashboard(request):
    return render(request, 'emailtool/audience_dashboard.html')

# Campaign Page
@login_required
def campaign_dashboard(request):
    return render(request, 'emailtool/campaign.html')

# Survey Page
@login_required
def survey_page(request):
    return render(request, 'emailtool/survey.html')

# Report Page
@login_required
def report_view(request):
    return render(request, 'emailtool/report.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'emailtool/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('audience_dashboard')

    else:
        form = LoginForm()
    return render(request, 'emailtool/login.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
# def thank_you(request):
#     # If you're submitting a form, you can pass data to the template like so
#     return render(request, 'thank_you.html')
# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def send_email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Getting form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Construct the email
            subject = f'New Message from {name}'
            message_body = f'From: {name}\nEmail: {email}\nMessage: {message}'

            # Send the email
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                ['sindhu060503@gmail.com'],  # Send to your email address
                fail_silently=False,
            )
            
            # Redirect to a success page or back to the form
            return redirect('email_sent')  # Create a success URL or view
            
    else:
        form = ContactForm()

    return render(request, 'emailtool/contact_form.html', {'form': form})
def email_sent_view(request):
    return render(request, 'emailtool/email_sent.html')
# views.py

from django.shortcuts import render, redirect
from .forms import SurveyForm

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # This is crucial
    else:
        form = SurveyForm()
    return render(request, 'emailtool/survey.html', {'form': form})

def thank_you(request):
    return render(request, 'emailtool/thank_you.html')


@login_required
def audience(request):
    contacts = Contact.objects.all()
    total_contacts = contacts.count()
    subscribed_contacts = contacts.filter(email_marketing=True).count()
    return render(request, 'emailtool/audience.html', {
        'contacts': contacts,
        'total_contacts': total_contacts,
        'subscribed_contacts': subscribed_contacts
    })
# from .models import AudienceMember

def audience_page(request):
    contacts = Contact.objects.all()
    return render(request, 'emailtool/audiencepage1.html', {'contacts': contacts})
def campaign_email_send(request):
    return render(request, 'emailtool/campaign_emailsend.html')
from django.contrib.auth.decorators import login_required

@login_required
def all_contacts_view(request):
    return render(request, 'emailtool/all_contacts.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
import csv

# Add Subscriber - Handles adding new contacts
@login_required
def add_subscriber(request, contact_id=None):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        birthday = request.POST.get('birthday')
        email_marketing = request.POST.get('email_marketing') == 'on'

        # Check if email already exists
        if Contact.objects.filter(email=email).exists():
            messages.error(request, 'A contact with this email already exists.')
            return redirect('all_contacts')

        # Create new contact
        Contact.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone_number=phone_number,
            birthday=birthday,
            email_marketing=email_marketing
        )

        messages.success(request, 'Contact added successfully!')
        return redirect('all_contacts')

    return render(request, 'emailtool/add_subscriber.html')

# Import Contacts from CSV - Handles importing contacts from a CSV file
def import_contacts(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader)  # Skip header if it exists
        for row in reader:
            if len(row) >= 3:
                name, email, status = row[0], row[1], row[2]
                Contact.objects.create(name=name, email=email, status=status)
        return redirect('all_contacts')
    return render(request, 'emailtool/import_contacts.html')

# Create Segment - Optional logic for creating segments (can be extended)
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def create_segment(request):
    if request.method == 'POST':
        segment_name = request.POST.get('segment_name')
        criteria = request.POST.get('criteria')
        # Add your segment creation logic here
        return redirect('audience')
    return render(request, 'emailtool/create_segment.html', {})

# All Contacts Page - Displays all contacts in the system
def all_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'emailtool/all_contacts.html', {'contacts': contacts})  # Change to your desired template name

# Edit Subscriber - Handles editing an existing contact
def edit_subscriber(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.status = request.POST.get('status')
        contact.save()
        return redirect('all_contacts')  # After editing, redirect back to the all contacts page
    return render(request, 'emailtool/add_subscriber.html', {'contact': contact})  # Pass contact for editing
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def delete_subscriber(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('all_contacts')  # Redirect back to all contacts page after delete
# from .models import AudienceMember  # adjust based on your actual model
@login_required
def audience_dashboard(request):
    return render(request, 'emailtool/audience_dashboard.html')
def AudienceMember(request):
    audience = AudienceMember.objects.all()
    return render(request, 'emailtool/audiencepage1.html', {'audience': audience})
from .models import Contact

def all_contacts_view(request):
    contacts = Contact.objects.all()
    return render(request, 'emailtool/all_contacts.html', {'contacts': contacts})

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddContactForm
from .models import Contact


# 


# added by A
def add_contact(request):
    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            # Print the cleaned form data
            print("First Name:", form.cleaned_data['first_name'])
            print("Last Name:", form.cleaned_data['last_name'])
            print("Email:", form.cleaned_data['email'])
            print("Phone:", form.cleaned_data.get('phone'))  # .get() in case it's optional

            form.save()
            return redirect('audiencepage1')
    else:
        form = AddContact()

    return render(request, 'emailtool/manage_contacts.html', {'form': form})



def toggle_subscription(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.subscription_status = not contact.subscription_status
    contact.save()
    return redirect('audiencepage1')

def overview(request):
    return render(request, 'emailtool/overview.html')
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def edit_contact(request, pk):
    # Get the contact to edit using the primary key (pk)
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        # If it's a POST request, validate and save the form
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()  # Save the updated contact data
            return redirect('audiencepage1')  # Redirect to the audience page after saving
    else:
        # If it's a GET request, display the form with the current contact data
        form = AddContactForm(instance=contact)

    return render(request, 'emailtool/edit_contact.html', {'form': form, 'contact': contact})


def audience_page(request):
    added_contacts = AddContact.objects.all()  # Get all contacts
    return render(request, 'emailtool/audiencepage1.html', {'added_contacts': added_contacts})

# views.py
def delete_contact(request, pk):
    contact = get_object_or_404(AddContact, pk=pk)  # Get the contact to delete
    contact.delete()  # Delete the contact
    return redirect('audiencepage1')  # Redirect to the audience page after deleting

# views.py
def manage_contacts(request):
    contacts = Contact.objects.all()  # Get all contacts
    return render(request, 'emailtool/manage_contacts.html', {'contacts': contacts})

# tages page 
from django.shortcuts import render

def tags(request):
    # Your logic for tags view
    return render(request, 'emailtool/tags.html')
from django.core.paginator import Paginator

def manage_contacts(request):
    contacts_list = Contact.objects.all().order_by('-id')
    paginator = Paginator(contacts_list, 5)  # Show 5 contacts per page

    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)

    return render(request, 'emailtool/manage_contacts.html', {'contacts': contacts})
# views.py
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Campaign


def campaign_details(request, title):
    campaign = get_object_or_404(Campaign, name=title)
    return render(request, 'emailtool/campaign_details.html', {'campaign': campaign})

def campaign_analytics(request, title):
    campaign = get_object_or_404(Campaign, name=title)
    return render(request, 'emailtool/analytics.html', {'campaign': campaign})

def campaign_actions(request, title):
    campaign = get_object_or_404(Campaign, name=title)
    return render(request, 'emailtool/actions.html', {'campaign': campaign})

from .models import Campaign
from .forms import CampaignForm

def edit_campaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    
    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('all_campaigns')  # Redirect to the list of campaigns
    else:
        form = CampaignForm(instance=campaign)

    return render(request, 'emailtool/edit_campaign.html', {'form': form, 'campaign': campaign})

# Add other views (edit, delete, etc.) as needed
from django.shortcuts import render, redirect
from .models import Campaign  # or your appropriate model

def delete_campaign(request, id):
    try:
        campaign = Campaign.objects.get(id=id)
        campaign.delete()
        return redirect('all_campaigns')  # Redirect to a list view or wherever appropriate
    except Campaign.DoesNotExist:
        return render(request, 'error.html', {'message': 'Campaign not found.'})
    
def all_campaigns(request):
    campaign_mails = SentEmail.objects.all().order_by('-sent_at')
    print('camp', campaign_mails)
    campaigns = Campaign.objects.all()
    return render(request, 'emailtool/all_campaigns.html', {'campaigns': campaigns,'campaign_mails':campaign_mails})
#
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailRecipientForm
from .models import EmailRecipient
from django.contrib import messages

def add_recipients(request):
    if request.method == 'POST':
        form = EmailRecipientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipient added successfully!')
            return redirect('add_recipients')
    else:
        form = EmailRecipientForm()
    recipients = EmailRecipient.objects.all()
    return render(request, 'emailtool/add_recipients.html', {'form': form, 'recipients': recipients})

def edit_recipient(request, pk):
    recipient = get_object_or_404(EmailRecipient, pk=pk)
    if request.method == 'POST':
        form = EmailRecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipient updated successfully!')
            return redirect('add_recipients')
    else:
        form = EmailRecipientForm(instance=recipient)
    return render(request, 'emailtool/add_recipients.html', {'form': form, 'recipient': recipient, 'recipients': EmailRecipient.objects.all()})

def delete_recipient(request, pk):
    recipient = get_object_or_404(EmailRecipient, pk=pk)
    if request.method == 'POST':
        recipient.delete()
        messages.success(request, 'Recipient deleted successfully!')
    else:
        messages.error(request, 'Invalid request method for deletion.')
    return redirect('add_recipients')

def send_emails(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', 'Test Email')
        message_template = request.POST.get('message', 'Hello {name},\n\nThis is a test email.')
        recipients = EmailRecipient.objects.filter(sent=False)
        sent_count = 0
        
        for recipient in recipients:
            personalized_message = message_template.format(name=recipient.name)
            try:
                send_mail(
                    subject,
                    personalized_message,
                    settings.EMAIL_HOST_USER,
                    [recipient.email],
                    fail_silently=False,
                )
                recipient.sent = True
                recipient.save()
                
                # Save the sent email details
                SentEmail.objects.create(
                    recipient_name=recipient.name,
                    recipient_email=recipient.email,
                    subject=subject,
                    message=personalized_message
                )
                
                sent_count += 1
            except Exception as e:
                messages.error(request, f"Failed to send email to {recipient.email}: {str(e)}")
        
        if sent_count > 0:
            messages.success(request, f"{sent_count} email(s) sent successfully!")
            return redirect('sent')  # Redirect to sent page after successful sending
        else:
            messages.info(request, 'No new recipients to send emails to.')
            return redirect('add_recipients')
    
    return render(request, 'emailtool/send_emails.html')

from django.shortcuts import render

def emailtemplate(request):
    return render(request, 'emailtool/emailtemplate.html')
# views.py

# emailtool/views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages  # Importing messages framework

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']  # Get the uploaded image
        fs = FileSystemStorage()  # Create an instance of FileSystemStorage
        filename = fs.save(image.name, image)  # Save the file with its name
        uploaded_file_url = fs.url(filename)  # Get the URL of the uploaded file

        # Show a success message
        messages.success(request, 'Image uploaded successfully!')  # Success message
        
        # After saving, render the template and pass the file URL to the context
        return render(request, 'emailtool/emailtemplate.html', {'uploaded_file_url': uploaded_file_url})
    
    return render(request, 'emailtool/emailtemplate.html')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import LinkButton

@csrf_exempt  # For fetch() requests (or use CSRF token)
def save_link(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            link = LinkButton.objects.create(
                type=data.get('type'),
                url=data.get('url'),
                new_tab=data.get('new_tab', False)
            )
            return JsonResponse({'status': 'success', 'id': link.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})
# emailmarketing/views.py
from django.shortcuts import render

def email_details_view(request, template_name):
    # Handle the logic for the 'details' view
    
     return render(request, 'emailtool/details.html', {'template_name': template_name})

def sent_view(request):
    sent_emails = SentEmail.objects.all().order_by('-sent_at')  # Get all sent emails, newest first
    return render(request, 'emailtool/sent.html', {'sent_emails': sent_emails})
# Homepage (Landing page)

from django.shortcuts import render
from .models import SentEmail

def sent_emails(request):
    sent_emails = SentEmail.objects.all().order_by('-sent_at')
    return render(request, 'sent_emails.html', {'sent_emails': sent_emails})




from django.shortcuts import render, redirect
from .forms import FeedbackForm  # rename your form class to FeedbackForm
from .models import Feedback  # keep model as Feedback
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Make sure URL pattern named 'thank_you' exists
    else:
        form = FeedbackForm()
    return render(request, 'emailtool/feedback.html', {'form': form})
def thank_you(request):
    return render(request, 'emailtool/thank_you.html')
def complete_feedback(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'emailtool/complete_feedback.html', {'feedbacks': feedbacks})