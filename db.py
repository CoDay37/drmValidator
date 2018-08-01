from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import socket

regex = regex.get()
try:
    self_client = MongoClient(host='18.207.154.217',port=27017)#creates client
except ServerSelectionTimeoutError:
    raise ServerSelectionTimeoutError('MongoDB is not current running on host server. \n Enter sudo service mongod restart')
if name:
