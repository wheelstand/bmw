from django.core.management import BaseCommand
from wheelstand.models import TestDrive
import requests
from requests.auth import HTTPBasicAuth
from django.core import serializers
import json


class Command(BaseCommand):

	def handle(self, *args, **options):
		url = 'http://dashboard.limelightplatform.com/limelight/integration/SubmitForm.json?formId=4712'
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		auth = HTTPBasicAuth('bmw+gmp@limelightplatform.com', 'demodemo')

		newdata = TestDrive.objects.filter(status=False)

		for i in newdata:
			payload = {
				'firstName' : i.first_name, 
				'lastName' : i.last_name, 
				'email' : i.language,
				'contact_method' : i.contact_method, 
				'phone' : i.phone, 
				'purchase_intent' : i.purchase_intent, 
				'brochure' : i.brochure, 
				'retailer_location' : i.retailer_location, 
				'retailer_number' : i.retailer_number, 
				'consent' : i.consent, 
				'vehicle' : i.vehicle, 
				'status' : i.status
#				'language': null 
			}
			print payload
			j = json.dumps(payload)
			print j
			r = requests.post(url, data=j, headers=headers, auth=auth)
			print r.status_code
			print r.text
			print i.status
			if r.status_code == 200:
				i.status = True
				i.save()
			print i.status			

