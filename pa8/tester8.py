# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
#
# The following command will test all test cases on your file:
#
#   python3 <thisfile.py> <your_one_file.py>
#
#
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
#
#   python3 <thisfile.py> <your_one_file.py> func1 func2
#
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
#
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
#
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
#
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time


############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.

REQUIRED_DEFNS = ['locateEmergency', 'pollingLocations', 'findMyLibrary', 'findPools']

# for method names in classes that will be tested
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = []

# how many points are test cases worth?
weight_required = 1
weight_extra_credit = 0

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 90

# how many seconds to wait between batch-mode gradings?
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode...
CURRENTLY_GRADING = False



# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):

	def setUpClass():
		cur_dir = files_list(".")
		assert os.path.abspath("hosp1.csv") in cur_dir, '\n\nunable to locate hosp1.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("hosp2.csv") in cur_dir, '\n\nunable to locate hosp2.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("hosp3.csv") in cur_dir, '\n\nunable to locate hosp3.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("police1.csv") in cur_dir, '\n\nunable to locate police1.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("police2.csv") in cur_dir, '\n\nunable to locate police2.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("police3.csv") in cur_dir, '\n\nunable to locate police3.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("precincts1.csv") in cur_dir, '\n\nunable to locate precincts1.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("precincts2.csv") in cur_dir, '\n\nunable to locate precincts2.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("precincts3.csv") in cur_dir, '\n\nunable to locate precincts3.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("voters1.csv") in cur_dir, '\n\nunable to locate voters1.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("voters2.csv") in cur_dir, '\n\nunable to locate voters2.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("voters3.csv") in cur_dir, '\n\nunable to locate voters3.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("libraries.csv") in cur_dir, '\n\nunable to locate libraries.csv!\nmove file to the current directory and try again.'
		assert os.path.abspath("pools.csv") in cur_dir, '\n\nunable to locate pools.csv!\nmove file to the current directory and try again.'

	############################################################################
	#locateEmergency Tests
	def test_locateEmergency_1(self):
		d = {'22101': [['Hospital', 'RESTON HOSPITAL CENTER', 'https://hcavirginia.com/locations/reston-hospital-center/', '1850 TOWN CENTER PKWY', '(703) 689-9000'], ['Police Station', 'McLean Station', '1437 Balls Hill RD', '703-556-7750']], '20121': [['Urgent Care', 'CENTREVILLE URGENT CARE', 'http://www.centrevilleurgentcare.com/home.html', '14001A SAINT GERMAIN DR', '(703) 830-8113']], '22310': [['Urgent Care', 'VIRGINIA HOSPITAL CENTER URGENT CARE', 'https://www.virginiahospitalcenter.com/medical-services/immediate-care/', '764 S 23RD ST', '(703) 717-7000'], ['Police Station', 'Franconia Station', '6121 Franconia RD', '703-922-0889']], '22306': [['Hospital', 'DOMINION HOSPITAL', 'https://hcavirginia.com/locations/dominion/', '2960 SLEEPY HOLLOW RD', '(703) 536-2000'], ['Hospital', 'INOVA FAIRFAX HOSPITAL', 'https://www.inova.org/locations/inova-fairfax-medical-campus', '3300 GALLOWS RD', '(703) 776-4001'], ['Police Station', 'Mt. Vernon Station', '2511 Parkers LN', '703-360-8400']], '20170': [['Police Station', 'Town of Herdon Station ', '397 Herndon PKWY', '703-435-6846']]}
		self.assertEqual(locateEmergency("hosp1.csv", "police1.csv"), d)

	def test_locateEmergency_2(self):
		d = {'22101': [['Hospital', 'RESTON HOSPITAL CENTER', 'https://hcavirginia.com/locations/reston-hospital-center/', '1850 TOWN CENTER PKWY', '(703) 689-9000']], '20121': [['Urgent Care', 'CENTREVILLE URGENT CARE', 'http://www.centrevilleurgentcare.com/home.html', '14001A SAINT GERMAIN DR', '(703) 830-8113']], '22310': [['Urgent Care', 'VIRGINIA HOSPITAL CENTER URGENT CARE', 'https://www.virginiahospitalcenter.com/medical-services/immediate-care/', '764 S 23RD ST', '(703) 717-7000'], ['Police Station', 'Fair Oaks Station', '12300 Lee Jackson Memorial HWY', '703-591-0966']], '22306': [['Hospital', 'DOMINION HOSPITAL', 'https://hcavirginia.com/locations/dominion/', '2960 SLEEPY HOLLOW RD', '(703) 536-2000'], ['Hospital', 'INOVA FAIRFAX HOSPITAL', 'https://www.inova.org/locations/inova-fairfax-medical-campus', '3300 GALLOWS RD', '(703) 776-4001']], '20170': [['Police Station', 'Town of Herdon Station ', '397 Herndon PKWY', '703-435-6846']], '22079': [['Police Station', 'City of Alexandria Station', '3600 Wheeler AVE', '703-746-4444']], '22046': [['Police Station', 'City of Falls Church Station', '300 Park AVE', '703-241-5050']], '20151': [['Police Station', 'West Springfield Station', '6140 Rolling RD', '703-644-7377']]}
		self.assertEqual(locateEmergency("hosp1.csv", "police2.csv"), d)

	def test_locateEmergency_3(self):
		d = {'22101': [['Hospital', 'RESTON HOSPITAL CENTER', 'https://hcavirginia.com/locations/reston-hospital-center/', '1850 TOWN CENTER PKWY', '(703) 689-9000']], '20121': [['Urgent Care', 'CENTREVILLE URGENT CARE', 'http://www.centrevilleurgentcare.com/home.html', '14001A SAINT GERMAIN DR', '(703) 830-8113']], '22310': [['Urgent Care', 'VIRGINIA HOSPITAL CENTER URGENT CARE', 'https://www.virginiahospitalcenter.com/medical-services/immediate-care/', '764 S 23RD ST', '(703) 717-7000']], '22306': [['Hospital', 'DOMINION HOSPITAL', 'https://hcavirginia.com/locations/dominion/', '2960 SLEEPY HOLLOW RD', '(703) 536-2000'], ['Hospital', 'INOVA FAIRFAX HOSPITAL', 'https://www.inova.org/locations/inova-fairfax-medical-campus', '3300 GALLOWS RD', '(703) 776-4001']], '22030': [['Police Station', 'City of Fairfax Station', '3730 Old Lee HWY', '703-385-7924']], '20190': [['Police Station', 'Reston Station', '1801 Cameron Glen DR', '703-478-0904']], '20151': [['Police Station', 'Sully Station', '4900 Stonecroft BLVD', '703-814-7000']], '22003': [['Police Station', 'Mason Station', '6507 Columbia PIKE', '703-256-8035']], '22180': [['Police Station', 'Town of Vienna Station ', '215 Center ST', '703-255-6366']]}
		self.assertEqual(locateEmergency("hosp1.csv", "police3.csv"), d)

	def test_locateEmergency_4(self):
		d = {'22151': [['Urgent Care', 'VUPC URGENT CARE', 'http://www.vupchealth.com/', '5501 BACKLICK RD', '(703) 564-5998']], '22079': [['Urgent Care', 'ALLCARE FAMILY MEDICINE & URGENT CARE - LORTON', 'https://allcarefamilymed.com/lorton-va', '7740 GUNSTON PLZ', '(703) 339-5858'], ['Hospital', 'INOVA HEALTHPLEX LORTON', 'https://www.inova.org/locations/inova-healthplex-lorton', '9321 SANGER ST', '(703) 982-8400']], '22310': [['Hospital', 'INOVA EMERGENCY ROOM - FRANCONIA/SPRINGFIELD', 'https://www.inova.org/locations/inova-emergency-room-healthplex-franconiaspringfield', '6355 WALKER LN', '(703) 797-6800'], ['Police Station', 'Franconia Station', '6121 Franconia RD', '703-922-0889']], '20151': [['Urgent Care', 'CARENOW URGENT CARE - CENTREVILLE', 'https://www.carenow.com/locations/northern-virginia/centreville/', '4995 WESTONE PLZ', '(571) 441-3980'], ['Urgent Care', 'CARENOW URGENT CARE - CHANTILLY', 'https://www.carenow.com/locations/northern-virginia/chantilly/', '3456 HISTORIC SULLY WAY', '(703) 435 3838']], '22101': [['Police Station', 'McLean Station', '1437 Balls Hill RD', '703-556-7750']], '22306': [['Police Station', 'Mt. Vernon Station', '2511 Parkers LN', '703-360-8400']], '20170': [['Police Station', 'Town of Herdon Station ', '397 Herndon PKWY', '703-435-6846']]}
		self.assertEqual(locateEmergency("hosp2.csv", "police1.csv"), d)

	def test_locateEmergency_5(self):
		d = {'22151': [['Urgent Care', 'VUPC URGENT CARE', 'http://www.vupchealth.com/', '5501 BACKLICK RD', '(703) 564-5998']], '22079': [['Urgent Care', 'ALLCARE FAMILY MEDICINE & URGENT CARE - LORTON', 'https://allcarefamilymed.com/lorton-va', '7740 GUNSTON PLZ', '(703) 339-5858'], ['Hospital', 'INOVA HEALTHPLEX LORTON', 'https://www.inova.org/locations/inova-healthplex-lorton', '9321 SANGER ST', '(703) 982-8400'], ['Police Station', 'City of Alexandria Station', '3600 Wheeler AVE', '703-746-4444']], '22310': [['Hospital', 'INOVA EMERGENCY ROOM - FRANCONIA/SPRINGFIELD', 'https://www.inova.org/locations/inova-emergency-room-healthplex-franconiaspringfield', '6355 WALKER LN', '(703) 797-6800'], ['Police Station', 'Fair Oaks Station', '12300 Lee Jackson Memorial HWY', '703-591-0966']], '20151': [['Urgent Care', 'CARENOW URGENT CARE - CENTREVILLE', 'https://www.carenow.com/locations/northern-virginia/centreville/', '4995 WESTONE PLZ', '(571) 441-3980'], ['Urgent Care', 'CARENOW URGENT CARE - CHANTILLY', 'https://www.carenow.com/locations/northern-virginia/chantilly/', '3456 HISTORIC SULLY WAY', '(703) 435 3838'], ['Police Station', 'West Springfield Station', '6140 Rolling RD', '703-644-7377']], '20170': [['Police Station', 'Town of Herdon Station ', '397 Herndon PKWY', '703-435-6846']], '22046': [['Police Station', 'City of Falls Church Station', '300 Park AVE', '703-241-5050']]}
		self.assertEqual(locateEmergency("hosp2.csv", "police2.csv"), d)

	def test_locateEmergency_6(self):
		d = {'22044': [['Hospital', 'DOMINION HOSPITAL', 'https://hcavirginia.com/locations/dominion/', '2960 SLEEPY HOLLOW RD', '(703) 536-2000']], '22042': [['Hospital', 'INOVA FAIRFAX HOSPITAL', 'https://www.inova.org/locations/inova-fairfax-medical-campus', '3300 GALLOWS RD', '(703) 776-4001']], '22030': [['Hospital', 'INOVA EMERGENCY CARE CENTER - FAIRFAX', 'https://www.inova.org/locations/inova-emergency-room-fairfax-city', '4315 CHAIN BRIDGE RD', '(703) 877-8200'], ['Police Station', 'City of Fairfax Station', '3730 Old Lee HWY', '703-385-7924']], '22304': [['Hospital', 'INOVA ALEXANDRIA HOSPITAL', 'https://www.inova.org/locations/inova-alexandria-hospital', '4320 SEMINARY RD', '(703) 504-3000']], '22015': [['Urgent Care', 'WALK IN MEDICAL CARE - BURKE', 'http://www.justwalkinmedicalcare.com/locations/burke/', '6045 BURKE CENTRE PKWY', '(703) 239-0300']], '22060': [['Hospital', 'FORT BELVOIR COMMUNITY HOSPITAL', 'https://tricare.mil/mtf/BelvoirHospital', '9300 DEWITT LOOP', '(571) 231-3224']], '22150': [['Urgent Care', 'DOMINION URGENT CARE', 'https://www.dominionurgentcare.com/', '6370 SPRINGFIELD PLZ', '(703) 569-7554']], '20190': [['Police Station', 'Reston Station', '1801 Cameron Glen DR', '703-478-0904']], '20151': [['Police Station', 'Sully Station', '4900 Stonecroft BLVD', '703-814-7000']], '22003': [['Police Station', 'Mason Station', '6507 Columbia PIKE', '703-256-8035']], '22180': [['Police Station', 'Town of Vienna Station ', '215 Center ST', '703-255-6366']]}
		self.assertEqual(locateEmergency("hosp3.csv", "police3.csv"), d)
	
	#pollingLocations Tests
	def test_pollingLocations_1(self):
		lst = ['Itai Tracee can vote at Hayfield Secondary School\nAddress: 7630 Telegraph Rd Alexandria, VA 22315', 'Soroush Inbal can vote at Crestwood Elementary School\nAddress: 6010 Hanover Ave Springfield, VA 22150', 'Okeanos Aloysius can vote at Robinson Secondary School\nAddress: 5035 Sideburn Rd Fairfax, VA 22032', 'Mawar Ealdwine can vote at Crestwood Elementary School\nAddress: 6010 Hanover Ave Springfield, VA 22150']
		self.assertEqual(pollingLocations("precincts1.csv", "voters1.csv"), lst)

	def test_pollingLocations_2(self):
		lst = ['Komang Iphigeneia can vote at Bren Mar Park Elementary School\nAddress: 6344 Beryl Rd Alexandria, VA 22312', 'Ludvig Eckhart can vote at Poe Middle School\nAddress: 7000 Cindy Ln Annandale, VA 22003', 'Bhumi Marlen can vote at Rolling Valley Elementary School\nAddress: 6703 Barnack Dr Springfield, VA 22152', 'Chanda Aebbe can vote at Keene Mill Elementary School\nAddress: 6310 Bardu Ave Springfield, VA 22152', 'Onesiphoros Viktor can vote at Fairview Elementary School\nAddress: 5815 Ox Rd Fairfax Station, VA 22039']
		self.assertEqual(pollingLocations("precincts2.csv", "voters2.csv"), lst)

	def test_pollingLocations_3(self):
		lst = ['Cortney Giselbert can vote at Cameron Elementary School\nAddress: 3434 Campbell Dr Alexandria, VA 22303', 'Taavetti Sigimar can vote at Bush Hill Elementary School\nAddress: 5927 Westchester St Alexandria, VA 22310', 'Isac Arjan can vote at Laurel Ridge Elementary School\nAddress: 10110 Commonwealth Blvd Fairfax, VA 22032', 'Bart Tanvi can vote at Robinson Secondary School\nAddress: 5035 Sideburn Rd Fairfax, VA 22032', 'Metztli Nadezda can vote at Fairview Elementary School\nAddress: 5815 Ox Rd Fairfax Station, VA 22039']
		self.assertEqual(pollingLocations("precincts3.csv", "voters3.csv"), lst)

	def test_pollingLocations_4(self):
		lst = ['Komang Iphigeneia can vote at Bren Mar Park Elementary School\nAddress: 6344 Beryl Rd Alexandria, VA 22312', 'Ludvig Eckhart can vote at Poe Middle School\nAddress: 7000 Cindy Ln Annandale, VA 22003']
		self.assertEqual(pollingLocations("precincts1.csv", "voters2.csv"), lst)

	def test_pollingLocations_5(self):
		lst = ['Bart Tanvi can vote at Robinson Secondary School\nAddress: 5035 Sideburn Rd Fairfax, VA 22032']
		self.assertEqual(pollingLocations("precincts1.csv", "voters3.csv"), lst)

	def test_pollingLocations_6(self):
		lst = ['Cortney Giselbert can vote at Cameron Elementary School\nAddress: 3434 Campbell Dr Alexandria, VA 22303', 'Taavetti Sigimar can vote at Bush Hill Elementary School\nAddress: 5927 Westchester St Alexandria, VA 22310', 'Isac Arjan can vote at Laurel Ridge Elementary School\nAddress: 10110 Commonwealth Blvd Fairfax, VA 22032', 'Bart Tanvi can vote at Robinson Secondary School\nAddress: 5035 Sideburn Rd Fairfax, VA 22032', 'Metztli Nadezda can vote at Fairview Elementary School\nAddress: 5815 Ox Rd Fairfax Station, VA 22039']
		self.assertEqual(pollingLocations("precincts2.csv", "voters3.csv"), lst)
	
	#findMyLibrary Tests
	def test_findMyLibrary_1(self):
		value = 'Library: PATRICK HENRY LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/patrick-henry\nAddress: 101 MAPLE AVE E VIENNA, VA 22180\nLibrary: POHICK REGIONAL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/pohick-regional\nAddress: 6450 SYDENSTRICKER RD BURKE, VA 22015\n'
		self.assertEqual(findMyLibrary("libraries.csv", "iCk"), value)

	def test_findMyLibrary_2(self):
		value = 'Library: PATRICK HENRY LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/patrick-henry\nAddress: 101 MAPLE AVE E VIENNA, VA 22180\nLibrary: POHICK REGIONAL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/pohick-regional\nAddress: 6450 SYDENSTRICKER RD BURKE, VA 22015\n'
		self.assertEqual(findMyLibrary("libraries.csv", "ICK"), value)

	def test_findMyLibrary_3(self):
		value = 'Library: GREAT FALLS LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/great-falls\nAddress: 9830 GEORGETOWN PIKE GREAT FALLS, VA 22066\n'
		self.assertEqual(findMyLibrary("libraries.csv", "Falls"), value)

	def test_findMyLibrary_4(self):
		value = 'Library: LORTON LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/lorton\nAddress: 9520 RICHMOND HWY LORTON, VA 22079\nLibrary: MARTHA WASHINGTON LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/martha-washington\nAddress: 6614 FORT HUNT RD ALEXANDRIA, VA 22307\nLibrary: RESTON REGIONAL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/reston-regional\nAddress: 11925 BOWMAN TOWNE DR RESTON, VA 20190\nLibrary: OAKTON LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/oakton\nAddress: 10304 LYNNHAVEN PL OAKTON, VA 22124\n'
		self.assertEqual(findMyLibrary("libraries.csv", "ton"), value)

	def test_findMyLibrary_5(self):
		value = 'Library: TYSONS-PIMMIT REGIONAL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/tysons-pimmit-regional\nAddress: 7584 LEESBURG PIKE FALLS CHURCH, VA 22043\nLibrary: CITY OF FAIRFAX REGIONAL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/city-of-fairfax-regional\nAddress: 10360 NORTH ST FAIRFAX, VA 22030\n'
		self.assertEqual(findMyLibrary("libraries.csv", "TY"), value)

	def test_findMyLibrary_6(self):
		value = 'Library: DOLLEY MADISON LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/dolley-madison\nAddress: 1244 OAK RIDGE AVE MCLEAN, VA 22101\nLibrary: THOMAS JEFFERSON LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/thomas-jefferson\nAddress: 7415 ARLINGTON BLVD FALLS CHURCH, VA 22042\nLibrary: GEORGE MASON REGIONAL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/george-mason-regional\nAddress: 7001 LITTLE RIVER TPKE ANNANDALE, VA 22003\nLibrary: JOHN MARSHALL LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/john-marshall\nAddress: 6209 ROSE HILL DR ALEXANDRIA, VA 22310\nLibrary: MARTHA WASHINGTON LIBRARY Website: https://www.fairfaxcounty.gov/library/branches/martha-washington\nAddress: 6614 FORT HUNT RD ALEXANDRIA, VA 22307\n'
		self.assertEqual(findMyLibrary("libraries.csv", "ma"), value)
	
	#findsPools Tests
	def test_findPools_1(self):
		val = "2 pools in zip code 22180:\n1)TOWNES OF MOOREFIELD SWIMMING POOL\n2)VIENNA AQUATIC CLUB SWIMMING POOL\n"
		self.assertEqual(findPools("pools.csv", 22180), val)

	def test_findPools_2(self):
		val = "4 pools in zip code 22030:\n1)COUNTRY CLUB OF FAIRFAX SWIMMING POOL\n2)ELMS AT OAKTON SWIMMING POOL\n3)FAIRFAX VILLAGE SWIMMING POOL\n4)OAKTON PARK SWIMMING POOL\n"
		self.assertEqual(findPools("pools.csv", 22030), val)

	def test_findPools_3(self):
		val = "12 pools in zip code 22041:\n1)BARCROFT HILLS SWIMMING POOL\n2)BARCROFT PLAZA SWIMMING POOL\n3)BARCROFT VIEW SWIMMING POOL\n4)GLEN FOREST SWIMMING POOL\n5)GRANDVIEW APARTMENTS SWIMMING POOL\n6)LAFAYETTE PARK SWIMMING POOL\n7)LAKESIDE PLAZA SWIMMING POOL\n8)OAKVIEW GARDENS SWIMMING POOL\n9)SAVOY PARK SWIMMING POOL\n10)SKYLINE SQUARE SWIMMING POOL\n11)SKYLINE TOWERS SWIMMING POOL\n12)WATERS EDGE SWIMMING POOL\n"
		self.assertEqual(findPools("pools.csv", 22041), val)

	def test_findPools_4(self):
		val = "9 pools in zip code 20190:\n1)CHESTNUT GROVE SWIMMING POOL\n2)COLVIN WOODS APARTMENT SWIMMING POOL\n3)GOLF COURSE ISLAND SWIMMING POOL\n4)HIDDEN CREEK COUNTRY CLUB SWIMMING POOL\n5)NORTH SHORE SWIMMING POOL\n6)OAK PARK SWIMMING POOL RESTON\n7)TALL OAKS SWIMMING POOL\n8)VANTAGE HILL SWIMMING POOL\n9)WATERMINE SWIMMING POOL\n"
		self.assertEqual(findPools("pools.csv", 20190), val)

	def test_findPools_5(self):
		val = "2 pools in zip code 22182:\n1)CHESTERBROOK ACADEMY SWIMMING POOL\n2)SHOUSE VILLAGE SWIMMING POOL\n"
		self.assertEqual(findPools("pools.csv", 22182), val)

	def test_findPools_6(self):
		val = "4 pools in zip code 22309:\n1)PINEWOOD LAWNS SWIMMING POOL\n2)ROLLING HILLS APARTMENTS SWIMMING POOL\n3)SACRAMENTO SQUARE SWIMMING POOL\n4)SEQUOYAH SWIMMING POOL\n"
		self.assertEqual(findPools("pools.csv", 22309), val)
		

	############################################################################

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		self.num_req = 0
		self.num_ec = 0
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]

				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))

#		print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test_extra_credit_".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if str(func).startswith("test_extra_credit_"+w):
						fs.append(AllTests(str(func)))

#			print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	this_file = __file__
	if dir==".":
		dir = os.getcwd()
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			if file==this_file:
				continue
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")

	if BATCH_MODE:
		print("BATCH MODE.\n")
		run_all()
		return

	else:
		want_all = len(sys.argv) <=2
		wants = []
		# remove batch_mode signifiers from want-candidates.
		want_candidates = sys.argv[2:]
		for i in range(len(want_candidates)-1,-1,-1):
			if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
				del want_candidates[i]

		# set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
		wants = []
		extra_credits = []
		if not want_all:
			for w in want_candidates:
				if w in REQUIRED_DEFNS:
					wants.append(w)
				elif w in SUB_DEFNS:
					wants.append(w)
				elif w in EXTRA_CREDIT_DEFNS:
					extra_credits.append(w)
				else:
					raise Exception("asked to limit testing to unknown function '%s'."%w)
		else:
			wants = REQUIRED_DEFNS + SUB_DEFNS
			extra_credits = EXTRA_CREDIT_DEFNS

		# now that we have parsed the function names to test, run this one file.
		run_one(wants,extra_credits)
		return
	return # should be unreachable!

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):

	has_reqs = len(wants)>0
	has_ec   = len(extra_credits)>0

	# make sure they exist.
	passed1 = 0
	passed2 = 0
	tried1 = 0
	tried2 = 0

	# only run tests if needed.
	if has_reqs:
		print("\nRunning required definitions:")
		(tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
	if has_ec:
		print("\nRunning extra credit definitions:")
		(tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)

	# print output based on what we ran.
	if has_reqs and not has_ec:
		print("\n%d/%d Required test cases passed" % (passed1,tried1) )
		'''print("\nScore based on test cases: %.2f/%d (%.2f*%d) " % (
																passed1*weight_required,
																total_points_from_tests,
																passed1,
																weight_required
															 ))'''
	elif has_ec and not has_reqs:
		print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
	else: # has both, we assume.
		print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
		print("\nScore based on test cases: %.2f / %d ( %d * %d + %d * %d) " % (
																passed1*weight_required+passed2*weight_extra_credit,
																total_points_from_tests,
																passed1,
																weight_required,
																passed2,
																weight_extra_credit
															 ))
	if CURRENTLY_GRADING:
		print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
		filenames = files_list(sys.argv[1])
		#print(filenames)

		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS

		results = []
		for filename in filenames:
			print(" Batching on : " +filename)
			# I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
			lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()

			# delay of shame...
			time.sleep(DELAY_OF_SHAME)

			name = os.path.basename(lines[-1])
			stuff =lines[-2].split(" ")[1:-1]
			print("STUFF: ",stuff, "LINES: ", lines)
			(passed_req, tried_req, passed_ec, tried_ec) = stuff
			results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
			continue

		print("\n\n\nGRAND RESULTS:\n")


		for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req).strip()
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible,
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))
# only used for batch mode.
def run_all_orig():
		filenames = files_list(sys.argv[1])
		#print(filenames)

		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS

		results = []
		for filename in filenames:
			# wipe out all definitions between users.
			for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
				globals()[fn] = decoy(fn)
				fn = decoy(fn)
			try:
				name = os.path.basename(filename)
				print("\n\n\nRUNNING: "+name)
				(tag_req, passed_req, tried_req) = run_file(filename,wants,False)
				(tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
				results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
				print(" ###### ", results)
			except SyntaxError as e:
				tag = filename+"_SYNTAX_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except NameError as e:
				tag =filename+"_Name_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ValueError as e:
				tag = filename+"_VALUE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except TypeError as e:
				tag = filename+"_TYPE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ImportError as e:
				tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except Exception as e:
				tag = filename+str(e.__reduce__()[0])
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))

# 			try:
# 				print("\n |||||||||| scrupe: "+str(scruples))
# 			except Exception as e:
# 				print("NO SCRUPE.",e)
# 			scruples = None

		print("\n\n\nGRAND RESULTS:\n")
		for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req)
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible,
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))

def try_copy(filename1, filename2, numTries):
	have_copy = False
	i = 0
	while (not have_copy) and (i < numTries):
		try:
			# move the student's code to a valid file.
			shutil.copy(filename1,filename2)

			# wait for file I/O to catch up...
			if(not wait_for_access(filename2, numTries)):
				return False

			have_copy = True
		except PermissionError:
			print("Trying to copy "+filename1+", may be locked...")
			i += 1
			time.sleep(1)
		except BaseException as e:
			print("\n\n\n\n\n\ntry-copy saw: "+e)

	if(i == numTries):
		return False
	return True

def try_remove(filename, numTries):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print("Trying to remove "+filename+", may be locked...")
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def wait_for_access(filename, numTries):
	i = 0
	while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
		print("Waiting for access to "+filename+", may be locked...")
		time.sleep(1)
		i += 1
	if(i == numTries):
		return False
	return True

# this will group all the tests together, prepare them as
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
	if wants==None:
		wants = []

	# move the student's code to a valid file.
	if(not try_copy(filename,"student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
		quit()

	# import student's code, and *only* copy over the expected functions
	# for later use.
	import importlib
	count = 0
	while True:
		try:
# 			print("\n\n\nbegin attempt:")
			while True:
				try:
					f = open("student.py","a")
					f.close()
					break
				except:
					pass
# 			print ("\n\nSUCCESS!")

			import student
			importlib.reload(student)
			break
		except ImportError as e:
			print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
			time.sleep(0.5)
			while not os.path.exists("student.py"):
				time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			print("SyntaxError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_SYNTAX_ERROR",None, None, None)
		except NameError as e:
			print("NameError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_Name_ERROR",0,1))
		except ValueError as e:
			print("ValueError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			print("TypeError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_TYPE_ERROR",0,1)
		except ImportError as e:
			print("ImportError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details or try again")
			return((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))
		except Exception as e:
			print("Exception in loading"+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+str(e.__reduce__()[0]),0,1)

	# make a global for each expected definition.
	for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			if fn in wants:
				print("\nNO DEFINITION FOR '%s'." % fn)

	if not checking_ec:
		# create an object that can run tests.
		runner = unittest.TextTestRunner()

		# define the suite of tests that should be run.
		suite = TheTestSuite(wants)


		# let the runner run the suite of tests.
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		# print(ans)

	else:
		# do the same for the extra credit.
		runner = unittest.TextTestRunner()
		suite = TheExtraCreditTestSuite(wants)
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		#print(ans)

	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	if(not try_remove("student.py", 5)):
		print("Failed to remove " + filename + " to student.py.")

	tag = ".".join(filename.split(".")[:-1])


	return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
		# this can accept any kind/amount of args, and will print a helpful message.
		def failyfail(*args, **kwargs):
			return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
		return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":

	main()
