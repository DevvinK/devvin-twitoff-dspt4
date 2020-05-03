# web_app/stats_routs.py

from flask import Blueprint, jsonify, request, flash, redirect#, render_template
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression # for example

stats_routes = Blueprint("stats_routes", __name__)


# TODO: accept some imputs related to the iris training data (x values)
@stats_routes.route("/stats/iris")
def iris():    
   X, y = load_iris(return_X_y=True)
   clf = LogisticRegression(random_state=0, solver="lbfgs",  multi_class="multinomial")
   clf.fit(X, y)

   result = str(clf.predict(X[:2, :]))
   print("Prediction", result)
   
   return result # TODO: return as JSON
