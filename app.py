from flask import Flask
import json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.json.ensure_ascii = False

with open("backup.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    # print(data)


class Data(Resource):
    def get(self):
        return data


api.add_resource(Data, "/data")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
