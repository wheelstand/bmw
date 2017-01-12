from django.core.management import BaseCommand
from wheelstand.models import KeepingInTouch
import requests
from requests.auth import HTTPBasicAuth
from django.core import serializers
import json


class Command(BaseCommand):

	def handle(self, *args, **options):
		url = 'http://dashboard.limelightplatform.com/limelight/integration/SubmitForm.json?formId=4833'
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		auth = HTTPBasicAuth('bmw+gmp@limelightplatform.com', 'demodemo')
		newdata = KeepingInTouch.objects.filter(status=False)

#		for i in newdata:
#			payload = serializers.serialize("json", [i])
#			r = requests.post(url, data=payload, headers=headers, auth=auth)
#			print r.status_code
#			print i.status
#			if r.status_code == 200:
#				i.status = True
#				i.save()

		for i in newdata:
			payload = {
				'firstName' : i.firstName, 
				'lastName' : i.lastName, 
				'email' : i.email,
				'language' : i.language, 
				'status' : i.status, 
				'phone' : i.phone, 
				'purchase_intent' : i.purchaseIntent, 			
				'consent' : i.consent, 
			}
			j = json.dumps(payload)
			r = requests.post(url, data=j, headers=headers, auth=auth)
			print r.status_code
			print r.text
			print i.status
			if r.status_code == 200:
				i.status = True
				i.save()
			print i.status			
