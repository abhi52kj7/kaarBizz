from flask import Flask, json, jsonify, request
from data import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def checkServer():
    return jsonify(result=True)

@app.route('/cars/all', methods=['GET'])
def getAllCarsNameApi():
    carsName = (getAllCarsName())
    return jsonify(carsName)

@app.route('/cars', methods=['GET'])
def getQueryCarsNameApi():
    query = request.args.get('q')
    carsName = getCarNameQuery(query)
    return jsonify(carsName)

@app.route('/dealers/nearme', methods=['GET'])
def getNeighbors():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    limit = request.args.get('limit')
    dealers = getNearestNeighbors(lat, lon, limit)
    file = json.dumps([ob.__dict__ for ob in dealers])
    return (file)
"""
@app.route('/dealers', methods=['GET'])
def getDealerFromId():
    id = request.args.get('id')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    dealers = getDealerById(id,lat,lon)
    file = json.dumps(dealers.__dict__)
    return (file)
"""
@app.route('/all', methods=['GET'])
def getSearchResults():
    query = request.args.get('q')
    searchResult = getSearchResultsFromQuery(query)
    file = json.dumps([ob.__dict__ for ob in searchResult])
    return file

@app.route('/dealers', methods=['GET'])
def getSearchDealersById():
    dtype = request.args.get('dtype')
    id = request.args.get('id')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    limit = request.args.get('limit')
    searchResult = getDealerById(dtype, id, lat, lon, limit)
    file = json.dumps([ob.__dict__ for ob in searchResult])
    return (file)    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
   