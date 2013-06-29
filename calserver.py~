import calendar, SimpleXMLRPCServer

#The server object
class Calendar:
    def getMonth(self, year, month):
        return calendar.month(year, month)

    def getYear(self, year):
        return calendar.calendar(year)

    def getName(self, name):
        return name

    """def getName(self):
        return "snehal here"""

calendar_object = Calendar()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8888))
server.register_instance(calendar_object)

#Go into the main listener loop
print "Listening on port 8888"
server.serve_forever()


