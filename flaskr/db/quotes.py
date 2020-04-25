from ramda import *
from flaskr.db import Quotes, Users


def addToDb(data):
    if not data:
        return 0
    else:
        added = Quotes.insert_many(data)
        return len(added.inserted_ids)


def returnQuote(quoteObject):
    return quoteObject['quote']


def getAll():
    retrievedQuotes = list(Quotes.find())
    quotesText = map(returnQuote, retrievedQuotes)

    return dict.fromkeys(set(quotesText), 0)


def markAsSeenByUser(details):
    user = Users.find_one({'_id': details['userId']})
    newSeenList = append(details['quoteId'], user['seenQuotes'])
    Users.update_one(
        {'_id': user['_id']},
        {'$set': {'seenQuotes': newSeenList}}
    )

    return 'OK'


def addToFavourites(details):
    user = Users.find_one({'_id': details['userId']})
    newFavouritesList = append(details['quoteId'], user['favouriteQuotes'])
    Users.update_one(
        {'_id': user['_id']},
        {'$set': {'seenQuotes': newFavouritesList}}
    )

    return 'OK'


def getById(quoteId):
    return Quotes.find_one({'_id': quoteId})


def getFavourites(userId):
    user = Users.find_one({'_id': userId})
    favouritesList = user['favouriteQuotes']

    return map(getById, favouritesList)


def getSeenForUser(userId):
    user = Users.find_one({'_id': userId})
    seenList = user['seenQuotes']

    return map(getById, seenList)


def getUnseenForUser(userId):
    user = Users.find_one({'_id': userId})
    seenList = user['seenQuotes']
    detailedSeenList = map(getById, seenList)
    seenTextList = map(returnQuote, detailedSeenList)

    seenQuotes = dict.fromkeys(set(seenTextList), 0)
    allQuotes = getAll()

    return without(seenQuotes, allQuotes)


def removeFromFavourites(details):
    user = Users.find_one({'_id': details['userId']})
    newFavouritesList = without(details['quoteId'], user['favouriteQuotes'])
    Users.update_one(
        {'_id': user['_id']},
        {'$set': {'seenQuotes': newFavouritesList}}
    )

    return 'OK'
