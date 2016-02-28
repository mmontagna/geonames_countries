import unittest, time
from geonames_countries import Countries

class TestCountries(unittest.TestCase):

  def test_findSingularProperties(self):
    self.assertEquals('Australia', Countries.findACountryBytld('.au'))
    self.assertEquals('AU', Countries.findAISOBytld('.au'))
    self.assertEquals('.au', Countries.findAtldByCountry('Australia'))

  def test_findManyProperties(self):
    countries = Countries.findISOByCurrencyCode('EUR')
    self.assertTrue('IE' in countries)
    self.assertTrue('IT' in countries)
    self.assertFalse('US' in countries) #What a day that'd be

    #Go on break the build ;)
    self.assertTrue('GB' in Countries.findISOByCurrencyCode('GBP'))

  def test_findDictionaries(self):
    countries = Countries.findByCurrencyCode('EUR')

    #We only get EUR
    self.assertTrue(all([x['CURRENCYCODE'] == 'EUR' for x in countries]))
    self.assertTrue('IT' in [x['ISO'] for x in countries])
    self.assertTrue('IE' in [x['ISO'] for x in countries])

if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCountries)
  unittest.TextTestRunner(verbosity=2).run(suite)