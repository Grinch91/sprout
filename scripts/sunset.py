import ephem
city=ephem.Observer()
city.lat='53.34'
city.long='-6.26'
s=ephem.Sun()
s.compute()
print ephem.localtime(city.next_setting(s))
print ephem.localtime(city.next_rising(s))
