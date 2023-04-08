from flask import Flask

app = Flask(__name__)

hackathons={
    "GHW: API Week":{
    "start_date":"2023-04-03 12:00:00",
    "end_date":"2023-04-10 12:00:00",
    "location":"Everywhere, Online",
    "type":"Digital Only"
    },
    "Bitcamp":{
    "start_date":"2023-04-07 12:00:00",
    "end_date":"2023-04-9 12:00:00",
    "location":"College Park, Maryland",
    "type":"In-Person Only"
    }
}
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/gethackathons", methods=['GET', 'POST'])
def gethackathons():
    if request.method=='POST':
        hackathons["New Hackathon"]=request.json
        return hackathons

    else:
        return hackathons