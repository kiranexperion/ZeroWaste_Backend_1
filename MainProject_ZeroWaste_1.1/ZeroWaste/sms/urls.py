from .import views
from django.urls import path
from .views import getPhoneNumberRegistered

urlpatterns = [

    path('send/',views.sendSMS,name = 'sms'),
    path('otp/', getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    

]