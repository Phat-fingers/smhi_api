import requests
import json
from settings import API_KEY


weather_symbol = {
        1: 'Clear sky',
        2: 'Nearly clear sky',
        3: 'Variable cloudiness',
        4: 'Halfclear sky',
        5: 'Cloudy sky',
        6: 'Overcast',
        7: 'Fog',
        8: 'Light rain showers',
        9: 'Moderate rain showers',
        10: 'Heavy rain showers',
        11: 'Thunderstorm',
        12: 'Light sleet showers',
        13: 'Moderate sleet showers',
        14: 'Heavy sleet showers',
        15: 'Light snow showers',
        16: 'Moderate snow showers',
        17: 'Heavy snow showers',
        18: 'Light rain',
        19: 'Moderate rain',
        20: 'Heavy rain',
        21: 'Thunder',
        22: 'Light sleet',
        23: 'Moderate sleet',
        24: 'Heavy sleet',
        25: 'Light snowfall',
        26: 'Moderate snowfall',
        27: 'Heavy snowfall',

}


class Smhi:

    def __init__(self, city):
        self.city = city

    """Get the long and lat from google maps api and"""
    def get_coordinates(self):
        self.resp = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?address={self.city}&key={API_KEY}').text
        self.data = json.loads(self.resp)
        self.lat = self.data['results'][0]['geometry']['location']['lat']
        self.lon = self.data['results'][0]['geometry']['location']['lng']
        #print(self.lat)

    """Get the data from smhi´s api"""
    def get_forcast(self):
        self.resp = requests.get(f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{self.lon:.2f}/lat/{self.lat:.2f}/data.json').text

        data = json.loads(self.resp)
        #print(data["timeSeries"][2]['parameters'][0]['values'])
        self.temp = "".join(map(str, data["timeSeries"][2]['parameters'][11]['values']))
        self.wind_speed = "".join(map(str, data["timeSeries"][2]['parameters'][14]['values']))
        self.wind_gust = "".join(map(str, data["timeSeries"][2]['parameters'][17]['values']))
        self.wcat = data["timeSeries"][2]['parameters'][18]['values']



    """Show the forcast from smhi's api"""
    def show_forcast(self):
        print(f'Prognos för {self.city} ')
        print(f'Temperatur: {self.temp}')
        print(f'Vind: {self.wind_speed} m/s, Vindbyar: {self.wind_gust} m/s')
        for k, v in weather_symbol.items():
            if k in self.wcat:
                print('Det är:', v)



if __name__ == '__main__':
    while True:
        city = input('Ange en stad: ').title()
        if city == 'q':
            break
        else:
            print('-' * 30)
            s = Smhi(city)
            s.get_coordinates()
            s.get_forcast()
            s.show_forcast()
            print('-' * 30)









