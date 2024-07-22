from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")

def emo_detector():
    ''' This code receives the text from the HTML interface and runs emotion detection over it using sentiment_analysis() function. The output returned shows the label and its confidence score for the provided text.'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    final_result = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 
    'sadness': sadness_score, 'dominant_emotion': dominant_emotion}

    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")

def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="0.0.0.0", port=5008)

