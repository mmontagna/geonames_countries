import json, gzip, os
from collections import defaultdict

class _Countries(object):

  def __init__(self):
    path = os.path.join(os.path.dirname(__file__), 'geonames_countries.json.gz')
    with gzip.open(path, 'r') as f:
      self.country_data = json.load(f)
    if (self.country_data['version'] != 0):
      raise Exception('geonames_countries.Countries got unknown geonames_countries.json.gz version.')
    self.countries = self.country_data['countries']
    self.header = self.country_data['header']

    self._dicts = [dict(zip(self.header, c)) for c in self.countries]
    self._indices = defaultdict(lambda: defaultdict(lambda: []))
    for country in self._dicts:
      for prop, val in country.iteritems():
        self._indices[prop][val].append(country)

  def _data(self):
    return self.country_data

  def dicts(self):
    return self._dicts

  def findXbyY(self, name, mark, delim):
      byIndex = name.index(delim)
      target = name[len(mark):byIndex].upper()
      source = name[byIndex + len(delim):].upper()
      return lambda x: [x[target] for x in self._indices[source][x]]

  def _getFirstOrNone(self, name, x):
    try:
      return self.findXbyY(name, 'findA', 'By')(x)[0]
    except:
      return None

  def __getattr__(self, name):
    if name.startswith('findBy'):
      prop = name[len('findBy'):].upper()
      return lambda x: self._indices[prop][x]
    if name.startswith('findA'):
      name = name
      return lambda x: self._getFirstOrNone(name, x)
    if name.startswith('find'):
      return self.findXbyY(name, 'find', 'By')
    else:
      return self.name
Countries = _Countries()