from django.db import models

from twilio.rest import Client

#defining a simple class
class SMS(models.Model):
    #integer field
    test_result = models.PositiveIntegerField()

    #string representation
    def __str__(self):
        return str(self.test_result)
    
 #save method
    def save(self,message,type):
                
        #twilio code
        account_sid = 'AC961ad7bef59a04ca6d1970c52ba1d247'
        auth_token = 'cba9ebdccb99c1122674f25a559e3f6b'
        client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #                                 body=f'Hello Customer your slot id is {self.test_result}. Your slot is today',
        #                                 from_='+15139604434',
        #                                 to='+91 86060 35533' 
        #                             )
        if type=='pickup':
            message = client.messages.create(  
                                messaging_service_sid='MG1a2a595d41785b16d725434e7a7f1b58', 
                                body='Hello Customer your slot id is'+message+' Your slot is today',      
                                to='+919188029461' 
                            ) 
            print(message.sid)
        else:
             message = client.messages.create(  
                                messaging_service_sid='MG1a2a595d41785b16d725434e7a7f1b58', 
                                body='OTP : '+message+' ZeroWaste uses this to verify your phone number',      
                                to='+919188029461' 
                            ) 
        return str(self.test_result)
    
# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    mobileNo = models.BigIntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification

    def __str__(self):
        return str(self.mobileNo)