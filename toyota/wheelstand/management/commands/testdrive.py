from django.core.management import BaseCommand
from wheelstand.models import TestDrive
import requests
from requests.auth import HTTPBasicAuth
from django.core import serializers


class Command(BaseCommand):

	def handle(self, *args, **options):
		url = 'http://endpoint.com'
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		auth = HTTPBasicAuth('user', 'pass')
#		newdata = serializers.serialize("json", TestDrive.objects.filter(status=False))

		newdata = TestDrive.objects.filter(status=False)

		for i in newdata:
			payload = serializers.serialize("json", [i])
			r = requests.post(url, data=payload, headers=headers, auth=auth)
			print r.status_code
			print r.text
			print i.status
			if r.status_code == 200:
				i.status = True
				i.save()
			print i.status
