from uszipcode import SearchEngine
engine = SearchEngine()
zipcode = engine.by_zipcode(301019)
print(zipcode.zipcode, zipcode.major_city, zipcode.population)
