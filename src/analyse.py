from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/analyse", methods=['POST','GET'])
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity
    es_blob = TextBlob(sentence).translate(to='zh-CN')
    return jsonify(
        sentence=sentence,
        spanishTranslation="{0}".format(es_blob),
        polarity=polarity
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
