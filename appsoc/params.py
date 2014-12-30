import settings

colors = {

    'about': '#000000',
    'contact': '#1C8FD1',
    'home': '#A60000',
    'learn': "#F78826",
    'register': '#A6E868',
}

post_limit = 10

mail_account = "icappsoc@gmail.com"

MONGO_URI = settings.MONGO_URI

MONGOENGINE_BACKEND = 'mongoengine.django.auth.MongoEngineBackend'

SESSION_AGE = 60 * 60 * 1

imperial_college_email_components = ['@ic.ac.uk', '@imperial.ac.uk']
