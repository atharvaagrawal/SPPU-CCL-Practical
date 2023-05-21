import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        number = 5
        table = ""
        for i in range(1, 11):
            result = number * i
            table += "{} x {} = {} <br/>".format(number, i, result)

        self.response.write(table)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
