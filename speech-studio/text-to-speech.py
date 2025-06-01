import azure.cognitiveservices.speech as speechsdk

speech_key = "<SUA_SPEECH_KEY>"
service_region = "<SUA_REGIÃO>"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioOutputConfig(filename="tts-sample.wav")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = "Olá, este é um exemplo de síntese de voz."
result = synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Áudio gerado com sucesso.")
else:
    print("Erro na síntese: {}".format(result.reason))
