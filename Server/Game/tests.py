from django.test import TestCase
from Game.models import Unit
from Communication.testhelper import *
import json

class TestUnit(TestCase):
	def setUp(self):
		self.channel = TestHelper()

	def test_create_unit_archer_success(self):
		logging.debug("==== Starting create unit archer success test ====")


		result = self.channel.createTestUser({"username": "archerowner", "password": "12345", "email": "archerowner@a.com"})
		self.assertTrue(result["Success"])

		result = self.channel.login({"token": result["Token"]})
		self.assertTrue(result["Success"])

		# Create the archer unit
		self.channel.send('{"Command":"UC","class":"Archer","owner":"archerowner","v":"1.0"}')
		result = self.channel.receive()
		self.assertEqual(result, json.dumps({"Success":True,"uid":Unit.objects.latest('pk').id}))