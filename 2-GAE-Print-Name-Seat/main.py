import webapp2


class Main(webapp2.RequestHandler):
    def get(self):
        for i in range(5):
            self.response.write(" Name: Atharva Agrawal <br>")
            self.response.write(" Rollno: 33303 <br>")
            self.response.write(" Department: IT <hr>")


app = webapp2.WSGIApplication(
    [("/", Main)]
)
