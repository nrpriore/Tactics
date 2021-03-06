from django.test import TestCase
from Communication.testhelper import *
from Static.create_data import *
import json

class TestStatic(CommonTestHelper):
	def test_db_01_bad_db_setup(self):
		result = setup_static_db("bad version")
		self.assertFalse(result)

	def test_il_02_v1_0(self):
		self.assertTrue(self.testHelper.createUserAndLogin(
			{"username":"init_user","password":self.testHelper.generateValidPassword(),"email":"initUser@email.com"}))

		self.testHelper.send('{"Command":"IL"}')
		result = self.testHelper.receive()

		expected_data = ver_1_0_static_data()

		self.maxDiff = None

		data = json.loads(result)
		expected_data = json.loads(json.dumps(expected_data))

		# Version Check - do the dictionaries match?
		self.assertEqual(data["Version"], expected_data["Version"])

		# Action Check - do the dictionaries match?
		self.assertEqual(data["Actions"], expected_data["Actions"])

		# Class Check - do the dictionaries match?
		self.assertEqual(data["Classes"], expected_data["Classes"])

		# Ability Check - do the dictionaries match?
		self.assertEqual(data["Abilities"], expected_data["Abilities"])

		# Leader Check - Ensure leader keys match, their values are not null, and ability lists, sorted, match
		for leader in data["Leaders"]:
			self.assertEqual(data["Leaders"][leader]["Description"],
				expected_data["Leaders"][leader]["Description"])
			abil_set = set(data["Leaders"][leader]["Abilities"]).intersection(expected_data["Leaders"][leader]["Abilities"])
			self.assertEqual(abil_set, set(data["Leaders"][leader]["Abilities"]))

		# Map Check - Ensure that each map name exists as a key, and its data is not null
		self.assertEqual(sorted(data["Maps"]), sorted(expected_data["Maps"]))
		for key in data["Maps"].keys():
			self.assertTrue(data["Maps"][key] != None)

			# Test that the map data matches what is saved in the file
			split_map = data["Maps"][key].split("n")
			with open(expected_data["Map_Base"] + expected_data["Maps"][key]) as file:
				counter = 0
				for line in file:
					self.assertTrue(split_map[counter] == line.strip())
					counter += 1

		# Perk Check - do the dictionaries match?
		self.assertEqual(data["Perks"], expected_data["Perks"])

		# Stat Check - do the dictionaries match?
		self.assertEqual(data["Stats"], expected_data["Stats"])

		# Terrain Check - do the dictionaries match?
		self.assertEqual(data["Terrain"], expected_data["Terrain"])

		# Verify the success
		self.assertEqual(data["Success"], True)

	def test_il_03_incomplete_version(self):
		self.assertTrue(self.testHelper.createUserAndLogin(
			{"username":"init_user","password":self.testHelper.generateValidPassword(),"email":"initUser@email.com"}))

		bad_ver = Version(name="bad version")
		bad_ver.save()

		self.testHelper.send('{"Command":"IL"}')
		result = self.testHelper.receive()
		logging.debug(result)

		self.assertEqual(result, json.dumps({"Success": False, "Error": "The following tables could not be loaded: Abilities, Actions, Classes, Leaders, Maps, Perks, Stats, Terrain"}))
