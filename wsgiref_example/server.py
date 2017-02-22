# server.py
from app import hello_world_app
from wsgiref.simple_server import make_server

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()
