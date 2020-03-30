from flask import Flask, render_template, request, make_response, Blueprint
import MySQLdb

from Admin.admin import app_admin as A
from Login.login import app_login as L
from View.view import app_view as V

app = Flask(__name__,  template_folder='../templates', static_folder='../static')


app.register_blueprint(A)
app.register_blueprint(L)
app.register_blueprint(V)


if __name__=='__main__':
  # app.run(debug=True)
  app.run(host='0.0.0.0', debug=True)


