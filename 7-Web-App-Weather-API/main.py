import webapp2
import urllib2
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
            <html>
            <body>
                <h2>Weather Forecast</h2>
                <form action="/weather" method="post">
                    <label for="latitude">Latitude:</label>
                    <input type="text" id="latitude" name="latitude"><br><br>
                    <label for="longitude">Longitude:</label>
                    <input type="text" id="longitude" name="longitude"><br><br>
                    <input type="submit" value="Get Forecast">
                </form>
            </body>
            </html>
        ''')


class WeatherHandler(webapp2.RequestHandler):
    def post(self):
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')

        if not latitude or not longitude:
            self.response.write('''
                <html>
                <body>
                    <h2>Error: Latitude and Longitude are required</h2>
                    <p>Please enter the latitude and longitude values.</p>
                    <a href="/">Go back</a>
                </body>
                </html>
            ''')
            return

        api_url = 'https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}'.format(
            latitude, longitude)

        response = urllib2.urlopen(api_url)
        data = json.load(response)

        print("Data:", data)
        forecast = data['forecast']

        self.response.write('''
            <html>
            <body>
                <h2>Weather Forecast</h2>
                <p>Latitude: {0}</p>
                <p>Longitude: {1}</p>
                <h3>Forecast:</h3>
        '''.format(latitude, longitude))

        for day in forecast:
            date = day['date']
            temperature = day['temperature']
            humidity = day['humidity']
            wind_speed = day['wind_speed']

            self.response.write('''
                <p>Date: {0}</p>
                <p>Temperature: {1} &#8451;</p>
                <p>Humidity: {2}%</p>
                <p>Wind Speed: {3} km/h</p>
                <br>
            '''.format(date, temperature, humidity, wind_speed))

        self.response.write('''
                <a href="/">Go back</a>
            </body>
            </html>
        ''')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/weather', WeatherHandler)
], debug=True)
