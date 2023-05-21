import webapp2
import os
from google.appengine.ext.webapp import template


class MainHandler(webapp2.RequestHandler):
    def get(self):
        name = "Your Name"
        seat_number = "123"
        department = "Your Department"

        res = []

        for _ in range(5):
            res.append({'name': name, 'seat_number': seat_number,
                       'department': department})

        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')

        self.response.out.write(template.render(path, {'res': res}))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
