#! /usr/bin/env python
from app import app
import os

os.system("sudo service postgresql start")
app.run(debug=True,host="0.0.0.0",port=8080)