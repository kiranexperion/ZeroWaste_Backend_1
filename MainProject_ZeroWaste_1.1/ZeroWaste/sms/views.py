from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from datetime import datetime
from .models import SMS
from rest_framework.views import APIView
from .models import phoneModel
import base64

# view for sending sms and otp

# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


#send sms to customers after the waste is picked up
@api_view(['POST'])
def sendSMS(request):
      # sms = SMS();
       message="10111"
     
      # sms.save(message,type="pickup");
       return Response({'status':1,'message':'Successfully Saved'})


#creating a OTP,sending OTP and verifying
class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request):
        phone=""
        try:
            Mobile = phoneModel.objects.get(mobileNo=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                mobileNo=phone,
            )
            Mobile = phoneModel.objects.get(mobileNo=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        sms = SMS()
        # sms.save(OTP.at(Mobile.counter),type="otp")
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request):
        phone="8606035533"
        try:
            Mobile = phoneModel.objects.get(mobileNo=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["OTP"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)

