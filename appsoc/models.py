from mongoengine import *


class Member(Document):
    event = StringField(required=False)
    email = StringField(required=True)


class Gsa(Document):
    event = StringField(required=False)
    email = StringField(required=True)
