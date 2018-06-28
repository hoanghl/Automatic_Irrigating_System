import pywapi

HCMC_WEATHER = pywapi.get_weather_from_weather_com('VMXX0007')


def get_sunrise():
    sunrise = (HCMC_WEATHER['forecasts'])[0]['sunrise']

    sunrise_hour = int(sunrise.split(':')[0])
    sunrise_min  = int((sunrise.split(':')[1]).split(' ')[0])

    return (sunrise_hour) + (sunrise_min * 1.0 / 60)

def get_sunset():
    sunset = (HCMC_WEATHER['forecasts'])[0]['sunset']

    sunset_hour = int(sunset.split(':')[0])
    sunset_min  = int((sunset.split(':')[1]).split(' ')[0])

    return (sunset_hour + 12) + (sunset_min * 1.0 / 60)

def daylight_propostion():
    """ Return the daylight percentage a day
    """
    
    return (get_sunset() - get_sunrise()) / 24


def get_temp():
    return int((HCMC_WEATHER['forecasts'])[0]['high']), int((HCMC_WEATHER['forecasts'])[0]['low'])


def watering_time_calculate():
    """ Calculate time for watering; 
    each 1 degree decreased needs 5 seconds
    each 1 degree increased needs 3 seconds 
    """
    hi, lo = get_temp()
    daylight = daylight_propostion()

    if daylight > 0.5:
        return int(((hi - daylight*(hi - lo)) - 26)*5)
    else:
        return int((((daylight*(hi - lo)) + lo) - 26)*3)

print watering_time_calculate()
