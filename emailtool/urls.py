from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('', views.home_view, name='home'),
    path('index/', views.index, name='index'),#graph1
    path('campaign/', views.campaign_dashboard, name='campaign'),
    #  path('survey/', views.survey_page, name='survey'),
         path('report/', views.report_view, name='report'),#graph2 
      path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('survey/', views.survey, name='survey'),
    path('thank-you/', views.thank_you, name='thank_you'),
#     path('audience/', views.audience_dashboard, name='audience_dashboard'),
    path('contact/', views.send_email_view, name='contact_form'),
    path('email_sent/', views.email_sent_view, name='email_sent'),
    #  path('thank-you/', views.thank_you, name='thank_you'),
     path('audience-aud/', views.audience_dashboard, name='audience'),
      path('audience/', views.audience_page, name='audiencepage'),
  path('campaign-send/', views.campaign_email_send, name='campaign_email_send'),
     path('all-contacts/', views.all_contacts_view, name='all_contacts'),
     path('all_contacts/add/', views.add_subscriber, name='add_subscriber'),
    path('all_contacts/import/', views.import_contacts, name='import_contacts'),
    path('all_contacts/segment/', views.create_segment, name='create_segment'),
     path('dashboard/', views.audience_dashboard, name='audience_dashboard'),  # Add this line
      path('add-contact/', views.add_contact, name='add_contact'),
       path('audience/', views.audience_page, name='audiencepage1'),
        #  path('edit-contact/<int:pk>/', views.manage_contacts, name='edit_contact'),    
        # path('delete-contact/<int:pk>/', views.delete_contact, name='delete_contact'),
       path('all_contacts/edit/<int:contact_id>/', views.edit_subscriber, name='edit_subscriber'),
        path('delete/<int:contact_id>/', views.delete_subscriber, name='delete_subscriber'),
        path('overview/', views.overview, name='overview'),
        path('tags/', views.tags, name='tags'),
      path('campaigns/', views.all_campaigns, name='all_campaigns'),
     path('edit-contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    # Details of a specific campaign
   path('campaigns/<str:title>/details', views.campaign_details, name='campaign_details'),
    path('campaigns/<str:title>/analytics', views.campaign_analytics, name='analytics'),
    path('campaigns/<str:title>/actions', views.campaign_actions, name='actions'),
    # Edit a specific campaign
    path('edit/<int:id>/', views.edit_campaign, name='edit_campaign'),
    path('emailtool/<str:template_name>/details/', views.email_details_view, name='email_details'),
    path('emailtool/<str:title>/analytics/', views.campaign_analytics, name='emailtool_analytics'),
    path('emailtool/<str:title>/actions/', views.campaign_actions, name='emailtool_actions'),
    # Delete a specific campaign
    path('delete/<int:id>/', views.delete_campaign, name='delete_campaign'),
    path('add_recipients/', views.add_recipients, name='add_recipients'),
    path('send/', views.send_emails, name='send_emails'),
    path('recipients/edit/<int:pk>/', views.edit_recipient, name='edit_recipient'),
    path('recipients/delete/<int:pk>/', views.delete_recipient, name='delete_recipient'),
    path('edit-contact/<int:pk>/', views.edit_contact, name='edit_contact'),
     path("emailtemplate/", views.emailtemplate, name="emailtemplate"),  # 👈 no comma!
     path('upload-image/', views.upload_image, name='upload_image'),
      path('save-link/', views.save_link, name='save_link'),
      path('sent/', views.sent_view, name='sent'),
    path('sent-emails/', views.sent_emails, name='sent_emails'),
    path('feedback/', views.feedback_view, name='feedback'),path('completed/', views.complete_feedback, name='complete_feedback'),
path('feedback/', views.feedback_view, name='feedback'),
path('completed/', views.complete_feedback, name='complete_feedback'),






    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)