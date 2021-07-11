perigee = 200000+6371000
apogee = 400000+6371000
sma = (perigee+apogee)/2
e = (apogee-perigee)/(2*sma)
print(e)
