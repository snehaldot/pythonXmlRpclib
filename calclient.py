import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")

month = server.getMonth(2002, 8)
"""name  = server.getName()"""
name = server.getName("sne")
print month
print name
