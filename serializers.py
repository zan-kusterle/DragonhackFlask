def serialize_result(r):
    return {
        'user_id': r.user_id,
        'score': r.score,
        'scores_by_time': r.scores_by_time
    }


def serialize_challenge(c):
    return {
        'from_user_id': c.from_user_id,
        'to_user_id': c.to_user_id,
        'pitches_by_time': c.pitches_by_time
    }
