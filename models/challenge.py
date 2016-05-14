from mongoengine import *


class Challenge(Document):
    from_user_id = StringField(required=True)
    to_user_id = StringField(required=True)
    pitches_by_time = ListField(FloatField, default=[])
