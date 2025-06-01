import azure.cognitiveservices.speech as speechsdk

# Configurações
speech_key = "<SUA_SPEECH_KEY>"
service_region = "<SUA_REGIÃO>"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_input = speechsdk.AudioConfig(filename="audio-sample.wav")
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

# Reconhecimento
result = recognizer.recognize_once()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Transcrição: {}".format(result.text))
else:
    print("Falha no reconhecimento: {}".format(result.reason))
