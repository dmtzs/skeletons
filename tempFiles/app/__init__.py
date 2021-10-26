try:
    from flask import Flask
except ImportError as eImp:
    print(f"The following import ERROR occurred: {eImp}")

app= Flask(__name__)

from app import routes, admin_routes