import requests
import json

def emotion_detector(text_to_analyze):
   # url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    emotion_prediction = formatted_response['emotionPredictions'][0]['emotion']
    
    dominant_emotion = max(emotion_prediction, key=emotion_prediction.get)
    anger_score = emotion_prediction['anger']
    disgust_score = emotion_prediction['disgust']
    fear_score = emotion_prediction['fear']
    joy_score = emotion_prediction['joy']
    sadness_score = emotion_prediction['sadness']

    result = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
              'sadness': sadness_score, 'dominant_emotion': dominant_emotion}

    return result


