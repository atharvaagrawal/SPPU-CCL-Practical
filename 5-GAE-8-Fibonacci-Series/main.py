import webapp2


def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


class MainHandler(webapp2.RequestHandler):
    def get(self):
        fib_series = fibonacci(8)
        self.response.write(fib_series)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
