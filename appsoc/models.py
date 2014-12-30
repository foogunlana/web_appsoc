from mongoengine import *


class Member(Document):
    email = StringField(required=True)
