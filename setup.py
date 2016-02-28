from distutils.core import setup

setup(
  name = 'geonames_countries',
  packages = ['geonames_countries'],
  version = '0.1',
  description = 'A simple wrapper for country code and tld data.',
  author = 'Marco Montagna',
  author_email = 'marcojoemontagna@gmail.com',
  url = 'https://github.com/mmontagna/geonames_countries',
  download_url = 'https://github.com/mmontagna/geonames_countries/archive/v0.1.tar.gz',
  keywords = ['tld', 'country code'],
  classifiers = [],
  include_package_data=True,
  package_data={'geonames_countries': ['geonames_countries.json.gz']}
)