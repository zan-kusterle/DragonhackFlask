import mongoengine
from flask import Flask, request, jsonify

from models.challenge import Challenge
from models.result import Result

app = Flask(__name__)

mongoengine.connect('sign_smart')


@app.route('/challenges', methods=['POST'])
def create_challenge():
    data = request.json

    challenge = Challenge(
        from_user_id=data['from_user_id'],
        to_user_id=data['to_user_id'],
        pitches_by_time=data['pitches_by_time']
    )
    challenge.save()

    return '', 201


@app.route('/challenges', methods=['GET'])
def get_challenges():
    to_user_id = request.args.get('to_user_id')

    challenges = Challenge.objects(to_user_id=to_user_id)

    return jsonify(challenges=challenges), 200


@app.route('/results', methods=['POST'])
def create_result():
    data = request.json

    result = Result(
        user_id=data['user_id'],
        score=data['score'],
        scores_by_time=data['scores_by_time']
    )
    result.save()

    return '', 201


@app.route('/results', methods=['GET'])
def get_results():
    user_id = request.args.get('user_id')

    results = Result.objects(user_id=user_id)

    return jsonify(results=results), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
