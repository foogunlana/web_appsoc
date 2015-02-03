from mongoengine import *


class Member(Document):
    event = StringField(required=False)
    email = StringField(required=True)
