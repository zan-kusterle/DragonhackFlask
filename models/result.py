from mongoengine import *


class Result(Document):
    user_id = StringField(required=True)
    score = FloatField(required=True)
    scores_by_time = ListField(FloatField, default=[])
