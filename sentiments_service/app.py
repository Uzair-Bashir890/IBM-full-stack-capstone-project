from flask import Flask, request, jsonify
import requests
import os


app = Flask(__name__)


WATSON_URL = os.getenv('WATSON_URL', 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


@app.route('/analyze', methods=['POST'])
def analyze():
data = request.json or {}
text = data.get('text', '')
if not text.strip():
return jsonify({"error":"empty text"}), 400
try:
# Call Watson service (the lab hosts it), fallback to simple rule if network error
r = requests.post(WATSON_URL, headers=HEADERS, json={"raw_document":{"text":text}}, timeout=5)
j = r.json()
# extract emotions
emotions = j['emotionPredictions'][0]['emotion']
except Exception as e:
# fallback: naive local scoring
emotions = { 'anger':0.0,'disgust':0.0,'fear':0.0,'joy':0.0,'sadness':0.0 }
low = text.lower()
if 'love' in low or 'happy' in low or 'glad' in low: emotions['joy'] = 0.9
if 'hate' in low or 'mad' in low: emotions['anger'] = 0.9
dominant = max(emotions, key=emotions.get)
output = dict(emotions)
output['dominant_emotion'] = dominant
return jsonify(output)


if __name__ == '__main__':
app.run(port=5001)