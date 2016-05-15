def serialize_result(r):
    return {
        'id': str(r.id),
        'challenge_id': r.challenge_id,
        'user_id': r.user_id,
        'score': r.score,
        'scores_by_time': r.scores_by_time
    }


def serialize_challenge(c):
    return {
        'id': str(c.id),
        'from_user_id': c.from_user_id,
        'to_user_id': c.to_user_id,
        'pitches_by_time': c.pitches_by_time
    }
