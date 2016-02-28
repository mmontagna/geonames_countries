[![Circle CI](https://circleci.com/gh/mmontagna/geonames_countries.svg?style=svg)](https://circleci.com/gh/mmontagna/geonames_countries)
[![Code Climate](https://codeclimate.com/github/mmontagna/geonames_countries/badges/gpa.svg)](https://codeclimate.com/github/mmontagna/geonames_countries)

#Geonames Countries

This package provides a simple wrapper around the
country data provided by [Geonames](http://download.geonames.org/export/dump/countryInfo.txt)

##How to install
```pip install geonames_countries```

##How to use

###Finding country codes which belong to a country that uses Euros
```
>>> from geonames_countries import Countries
>>> Countries.findISOByCurrencyCode('EUR')
[u'AD', u'AT', u'AX', u'BE', u'BL', u'CY', u'DE', u'EE', u'ES', u'FI', u'FR', u'GF', u'GP', u'GR', u'IE', u'IT', u'XK', u'LT', u'LU', u'LV', u'MC', u'ME', u'MF', u'MQ', u'MT', u'NL', u'PM', u'PT', u'RE', u'SI', u'SK', u'SM', u'TF', u'VA', u'YT']

```
###Finding the country associated with a tld
```
>>> from geonames_countries import Countries
>>> Countries.findCountryBytld('.au')
[u'Australia']

```

###Getting a country dict
```
>>> from geonames_countries import Countries
>>> Countries.findBytld('.au')
[{u'GEONAMEID': u'2077456', u'COUNTRY': u'Australia', u'CURRENCYCODE': u'AUD', u'TLD': u'.au', u'POSTAL CODE FORMAT': u'####', u'LANGUAGES': u'en-AU', u'PHONE': u'61', u'ISO3': u'AUS', u'FIPS': u'AS', u'CAPITAL': u'Canberra', u'POSTAL CODE REGEX': u'^(\\d{4})$', u'ISO': u'AU', u'ISO-NUMERIC': u'036', u'AREA(IN SQ KM)': u'7686850', u'CURRENCYNAME': u'Dollar', u'CONTINENT': u'OC', u'POPULATION': u'21515754'}]

```

Update the geonames_countries data by running `update_country_data`.


Geonames, and by extension this project, licenses their data under the [Creative Commons Attribution 3.0 License][http://creativecommons.org/licenses/by/3.0/].