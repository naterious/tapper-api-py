from flask import Response, request, jsonify
from json import dumps

from flaskr import create_app
from flaskr.db import facts
from flaskr.db import quotes

app = create_app()


def createResponse(body):
    response = Response(dumps(body), mimetype='application/json; charset=utf-8')
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route('/facts')
def getAllFactsMethod():
    result = facts.getAll()
    return createResponse(result)


@app.route('/facts/seen', methods=['POST'])
def markFactAsSeenByUserMethod():
    result = facts.markAsSeenByUser(request.get_json())
    return createResponse(result)


@app.route('/facts/liked', methods=['POST'])
def addFactToFavouritesMethod():
    result = facts.addToFavourites(request.get_json())
    return createResponse(result)


@app.route('/facts/<userId>/new')
def getUnseenFactsMethod(userId):
    result = facts.getUnseenForUser(userId)
    return createResponse(result)


@app.route('/facts/<userId>/favourites')
def getFavouriteFactsMethod(userId):
    result = facts.getUnseenForUser(userId)
    return createResponse(result)


@app.route('/facts/<userId>/seen')
def getSeenFactsMethod(userId):
    result = facts.getSeenForUser(userId)
    return createResponse(result)


@app.route('/facts/fact/<factId>')
def getFactByIdMethod(factId):
    result = facts.getById(factId)
    return createResponse(result)


@app.route('/facts/liked', methods=['DELETE'])
def removeFactFromFavouritesMethod():
    result = facts.removeFromFavourites(request.get_json())
    return createResponse(result)


@app.route('/quotes')
def getAllQuotesMethod():
    result = quotes.getAll()
    return createResponse(result)


@app.route('/quotes/seen', methods=['POST'])
def markQuoteAsSeenByUserMethod():
    result = quotes.markAsSeenByUser(request.get_json())
    return createResponse(result)


@app.route('/quotes/liked', methods=['POST'])
def addQuoteToFavouritesMethod():
    result = quotes.addToFavourites(request.get_json())
    return createResponse(result)


@app.route('/quotes/<userId>/new')
def getUnseenQuotesMethod(userId):
    result = quotes.getUnseenForUser(userId)
    return createResponse(result)


@app.route('/quotes/<userId>/favourites')
def getFavouriteQuotesMethod(userId):
    result = quotes.getUnseenForUser(userId)
    return createResponse(result)


@app.route('/quotes/<userId>/seen')
def getSeenQuotesMethod(userId):
    result = quotes.getSeenForUser(userId)
    return createResponse(result)


@app.route('/quotes/fact/<quoteId>')
def getQuoteByIdMethod(quoteId):
    result = quotes.getById(quoteId)
    return createResponse(result)


@app.route('/quotes/liked', methods=['DELETE'])
def removeQuoteFromFavouritesMethod():
    result = quotes.removeFromFavourites(request.get_json())
    return createResponse(result)


if __name__ == '__main__':
    app.run()
