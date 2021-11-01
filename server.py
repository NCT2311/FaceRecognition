import os
import flask
import mongodb

# Query from DB and export to JSON to excute
mongodb.queryFromDB()

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '''Test API'''

@app.route("/api/...", methods = ["GET"])
def queryUsers():
    '''Get user'''
    #https://stackoverflow.com/questions/21133976/flask-load-local-json
    SITEROOT = os.path.realpath(os.path.dirname(__file__))
    jsonUrl = os.path.join(SITEROOT, "users.json")
    userList = flask.json.load(open(jsonUrl, "r"))
    return flask.jsonify(userList)

if __name__ == '__main__':
    app.run()