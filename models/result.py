from mongoengine import *


class Result(Document):
    challenge_id = StringField(required=True)
    user_id = StringField(required=True)
    score = FloatField(required=True)
    scores_by_time = ListField(FloatField, default=[])
