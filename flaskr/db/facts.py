from ramda import *
from flaskr.db import Facts, Users


def addToDb(data):
    if not data:
        return 0
    else:
        added = Facts.insert_many(data)
        return len(added.inserted_ids)


def returnFact(factObject):
    return factObject['fact']


def getAll():
    retrievedFacts = list(Facts.find())
    factsText = map(returnFact, retrievedFacts)

    return factsText


def markAsSeenByUser(details):
    user = Users.find_one({'_id': details['userId']})
    newSeenList = append(details['factId'], user['seenFacts'])
    Users.update_one(
        {'_id': user['_id']},
        {'$set': {'seenFacts': newSeenList}}
    )

    return 'OK'


def addToFavourites(details):
    user = Users.find_one({'_id': details['userId']})
    newFavouritesList = append(details['factId'], user['favouriteFacts'])
    Users.update_one(
        {'_id': user['_id']},
        {'$set': {'seenFacts': newFavouritesList}}
    )

    return 'OK'


def getById(factId):
    return Facts.find_one({'_id': factId})


def getFavourites(userId):
    user = Users.find_one({'_id': userId})
    favouritesList = user['favouriteFacts']

    return map(getById, favouritesList)


def getSeenForUser(userId):
    user = Users.find_one({'_id': userId})
    seenList = user['seenFacts']

    return map(getById, seenList)


def getUnseenForUser(userId):
    user = Users.find_one({'_id': userId})
    seenList = user['seenFacts']
    detailedSeenList = map(getById, seenList)
    seenTextList = map(returnFact, detailedSeenList)

    seenFacts = dict.fromkeys(set(seenTextList), 0)
    allFacts = getAll()

    return without(seenFacts, allFacts)


def removeFromFavourites(details):
    user = Users.find_one({'_id': details['userId']})
    newFavouritesList = without(details['factId'], user['favouriteFacts'])
    Users.update_one(
        {'_id': user['_id']},
        {'$set': {'seenFacts': newFavouritesList}}
    )

    return 'OK'
