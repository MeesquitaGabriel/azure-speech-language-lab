from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "<SUA_LANGUAGE_KEY>"
endpoint = "<SEU_LANGUAGE_ENDPOINT>"
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documentos = [
    "A Microsoft anunciou novos recursos de IA em junho de 2025.",
    "A equipe de marketing viajará para São Paulo no próximo mês."
]

# Sentiment Analysis
response_sentiment = client.analyze_sentiment(documents=documentos)
for doc in response_sentiment:
    print(f"Documento: '{doc.id}'")
    print(f"Sentimento Global: {doc.sentiment}")
    for idx, sentence in enumerate(doc.sentences):
        print(f"  Sentença {idx} Sentimento: {sentence.sentiment} (score: {sentence.confidence_scores})")

# Key Phrase Extraction
response_keyphrases = client.extract_key_phrases(documents=documentos)
for doc in response_keyphrases:
    print(f"Documento: '{doc.id}' → Key Phrases: {doc.key_phrases}")

# Named Entity Recognition
response_ner = client.recognize_entities(documents=documentos)
for doc in response_ner:
    print(f"Documento: '{doc.id}' → Entidades:")
    for ent in doc.entities:
        print(f"  - {ent.text} ({ent.category})")
