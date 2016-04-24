from flask import Flask, request
import flask
from flask_restful import Resource, Api
from datetime import timedelta, date
from weather_service import GetWeather, GetSimilarDates, GetPastForDate
from emotion_service import AnalyzeEmotions
from main_controller import GetAllMyShit
from datetime import timedelta
import json

app = Flask(__name__)
api = Api(app)

class FindCurrentWeather(Resource):
        def GetCurrentWeather(self, request):
                location = request.values['location']
                dateString = request.values['dateString']
                weather = GetWeather(location, dateString)
                return weather

        def post(self):
                return json.dumps(self.GetCurrentWeather(request))
                                
class FindPastForDate(Resource):
    def post(self):
        data = json.loads(request.data)
        location = data['location']
        dateString = data['date']
        years = data['years']
        desiredDelta = timedelta(weeks=52*years)
        datesInfo = GetPastForDate(location, dateString, desiredDelta)
        return json.dumps(datesInfo)
    
    
class FindSimilarDates(Resource):
        def GetMatchingWeather(self, request):
                location = request.values['location']
                dateString = request.values['dateString']
                dates = GetSimilarDates(location, 10, dateString)
                return dates

        def post(self):
                return self.GetMatchingWeather(request)                                                                                     

class FindEmotionalContent(Resource):
    def post(self):
        data = json.loads(request.data)
        imageUrls = data['imageUrls']
        return AnalyzeEmotions(imageUrls)
        

class GetImagesAndData(Resource):
    def post(self):
        data = json.loads(request.data)
        location = data['location']
        date = data['date']
        token = data['token']
        num_matches = data['numDates']
        search_size = data['search_size']
        returnValues = GetAllMyShit(location, date, token, search_size,num_matches)
        headers = {'Access-Control-Allow-Headers':'Content-Type','Access-Control-Allow-Methods':'GET, POST, OPTIONS', 'Access-Control-Allow-Origin': '*'}
        resp = flask.Response(json.dumps(returnValues))
    #    resp.headers.add('Access-Control-Allow-Headers', 'Cache-Control, Pragma, Origin, Authorization, Content-Type, X-Requested-With')
     #   resp.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT')
        #resp.headers.add('Access-Control-Allow-Origin', 'http://localhost:3333')
       # resp.headers.add('Access-Control-Allow-Credentials', 'true')
        return resp
    @app.after_request
    def after_request(response):
       response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3333')
       response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Requested-With')
       response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
       response.headers.add('Access-Control-Allow-Credentials', 'true')
       return response
        

api.add_resource(FindCurrentWeather, "/FindCurrentWeather")
api.add_resource(FindSimilarDates, "/FindSimilarDates")
api.add_resource(FindPastForDate, "/FindPastForDate")
api.add_resource(FindEmotionalContent, "/GetEmotionalContent")
api.add_resource(GetImagesAndData, "/GetAllMyShit")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
