from flask import Response, request
from json import dumps

from flaskr import create_app
from flaskr.db import facts
from flaskr.db import quotes

app = create_app()


@app.route('/facts')
def getAllFactsMethod():
    factsList = facts.getAll()
    return Response(dumps(factsList), mimetype='application/json')


@app.route('/facts/seen', methods=['POST'])
def markFactAsSeenByUserMethod():
    return facts.markAsSeenByUser(request.get_json())


@app.route('/facts/liked', methods=['POST'])
def addFactToFavouritesMethod():
    return facts.addToFavourites(request.get_json())


@app.route('/facts/<userId>/new')
def getUnseenFactsMethod(userId):
    return facts.getUnseenForUser(userId)


@app.route('/facts/<userId>/favourites')
def getFavouriteFactsMethod(userId):
    return facts.getUnseenForUser(userId)


@app.route('/facts/<userId>/seen')
def getSeenFactsMethod(userId):
    return facts.getSeenForUser(userId)


@app.route('/facts/fact/<factId>')
def getFactByIdMethod(factId):
    return facts.getById(factId)


@app.route('/facts/liked', methods=['DELETE'])
def removeFactFromFavouritesMethod():
    return facts.removeFromFavourites(request.get_json())


@app.route('/quotes')
def getAllQuotesMethod():
    quotesList = quotes.getAll()
    return Response(dumps(quotesList), mimetype='application/json')


@app.route('/quotes/seen', methods=['POST'])
def markQuoteAsSeenByUserMethod():
    return quotes.markAsSeenByUser(request.get_json())


@app.route('/quotes/liked', methods=['POST'])
def addQuoteToFavouritesMethod():
    return quotes.addToFavourites(request.get_json())


@app.route('/quotes/<userId>/new')
def getUnseenQuotesMethod(userId):
    return quotes.getUnseenForUser(userId)


@app.route('/quotes/<userId>/favourites')
def getFavouriteQuotesMethod(userId):
    return quotes.getUnseenForUser(userId)


@app.route('/quotes/<userId>/seen')
def getSeenQuotesMethod(userId):
    return quotes.getSeenForUser(userId)


@app.route('/quotes/fact/<quoteId>')
def getQuoteByIdMethod(quoteId):
    return quotes.getById(quoteId)


@app.route('/quotes/liked', methods=['DELETE'])
def removeQuoteFromFavouritesMethod():
    return quotes.removeFromFavourites(request.get_json())


if __name__ == '__main__':
    app.run()
