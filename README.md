# Azure Speech & Language Lab

**Descrição Geral:**  
Este repositório contém toda a documentação, scripts e capturas de tela referentes ao laboratório de prática com Azure Speech Studio e Language Studio. O objetivo é demonstrar como configurar, consumir e explorar os serviços de fala e linguagem natural da Azure, além de registrar insights e aprendizados.

---

## Sumário

1. [Objetivos do Desafio](#objetivos-do-desafio)  
2. [Pré-requisitos](#pré-requisitos)  
3. [Visão Geral das Ferramentas](#visão-geral-das-ferramentas)  
   - [Azure Speech Studio](#azure-speech-studio)  
   - [Azure Language Studio](#azure-language-studio)  
4. [Passo a Passo do Laboratório](#passo-a-passo-do-laboratório)  
   1. [Configuração do Ambiente](#configuração-do-ambiente)  
   2. [Experimentando o Speech-to-Text](#experimentando-o-speech-to-text)  
   3. [Text-to-Speech e Voz Personalizada](#text-to-speech-e-voz-personalizada)  
   4. [Análise de Texto com Language Studio](#análise-de-texto-com-language-studio)  
5. [Código e Exemplos](#código-e-exemplos)  
   - [Scripts de Exemplo](#scripts-de-exemplo)  
   - [Notebooks de Demonstração](#notebooks-de-demonstração)  
6. [Capturas de Tela](#capturas-de-tela)  
7. [Desafios Encontrados e Soluções](#desafios-encontrados-e-soluções)  
8. [Próximos Passos / Recomendações](#próximos-passos--recomendações)  
9. [Referências Úteis](#referências-úteis)  

---

## Objetivos do Desafio

- Praticar a utilização das ferramentas Azure Speech Studio e Language Studio.  
- Documentar o processo técnico de forma clara, usando Markdown.  
- Utilizar o GitHub como repositório de compartilhamento de documentação técnica.

## Pré-requisitos

Antes de começar, certifique-se de ter:
- Uma assinatura ativa da Azure (também é possível usar a camada gratuita, se disponível).  
- Permissões para criar recursos de Speech e Language no portal Azure.  
- VS Code, PowerShell/Terminal, ou qualquer editor de sua preferência.  
- Conta no GitHub para criar e versionar este repositório.  
- (Opcional) Familiaridade inicial com Git: `clone`, `commit`, `push`.

---

## Visão Geral das Ferramentas

### Azure Speech Studio

O **Azure Speech Studio** fornece uma interface web para:
1. **Speech-to-Text (Reconhecimento de Fala)**  
2. **Text-to-Speech (Síntese de Voz)**  
3. **Custom Voice (Voz Customizada)**  
4. **Speech Translation (Tradução de Fala)**  

Principais usos:
- Transcrever gravações de áudio em texto.  
- Gerar arquivos de áudio sintetizando textos.  
- Criar e treinar modelos de voz personalizados.

### Azure Language Studio

O **Azure Language Studio** concentra-se em processamento de linguagem natural:
1. **Análise de Sentimento**  
2. **Extração de Informações (Key Phrases, Entidades)**  
3. **Classificação de Texto**  
4. **Reconhecimento de Entidades Nomeadas (NER)**  
5. **Extração de Resumo**  

Permite testes rápidos pela interface web e exportação de exemplos de payloads JSON, além de chamadas via API/SDK.

---

## Passo a Passo do Laboratório

### Configuração do Ambiente

1. **Criar Resource Group**  
   - No Azure Portal, clique em “Resource Groups” → “+ Create” → nomeie como `rg-speech-language-lab` → selecione região (por exemplo, East US) → Review + Create.

2. **Provisionar Serviço de Speech**  
   - No Azure Portal, “Create a resource” → “Speech” → escolha “Speech Services”.  
   - Preencha:  
     - Nome: `svc-speech-lab`  
     - Resource Group: `rg-speech-language-lab`  
     - Região: a mesma usada anteriormente  
     - Pricing Tier: F0 (gratuito) ou S0 (padrão)  
   - Após criado, acesse → “Keys and Endpoint” e copie ambas as chaves e o endpoint para uso posterior.

3. **Provisionar Serviço de Language (Azure OpenAI ou Text Analytics)**  
   - No Azure Portal, “Create a resource” → “Language” → “Language Resources” (para Text Analytics).  
   - Preencha:  
     - Nome: `svc-language-lab`  
     - Resource Group: `rg-speech-language-lab`  
     - Região: igual ao Speech  
     - Pricing Tier: F0 (gratuito) ou S0.  
   - Após criado, acesse → “Keys and Endpoint” e copie também as credenciais.

4. **Instalar SDKs (opcional)**  
   - Se for usar Python:  
     \`\`\`bash  
     pip install azure-cognitiveservices-speech azure-ai-textanalytics  
     \`\`\`  
   - Se for usar C#:  
     \`\`\`powershell  
     Install-Package Microsoft.CognitiveServices.Speech  
     Install-Package Azure.AI.TextAnalytics  
     \`\`\`  
   - Documente os passos de instalação na seção “Pré-requisitos” ou em um arquivo separado (`requirements.txt` ou `packages.config`).

---

### Experimentando o Speech-to-Text

1. **Exemplo na Interface Web (Speech Studio)**  
   - Acesse https://speech.microsoft.com/.  
   - Faça login e escolha “Speech-to-text” → “Transcription”.  
   - Faça upload de um arquivo de áudio (por exemplo, `audio-sample.wav`).  
     ![speech-studio-setup.png](images/speech-studio-setup.png)  
   - Observe o texto transcrito e exporte como JSON caso queira salvar o output (coloque em `/speech-studio/transcript-example.json`).

2. **Exemplo via Código (Python)**  
   - Crie um arquivo `speech-to-text.py` e documente o código:  
     \`\`\`python  
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
     \`\`\`  
   - Inclua observações no `README.md`:  
     - Como configurar variáveis de ambiente (Speech Key, Region).  
     - Interpretação do objeto `result` (podem haver erros, ruídos, falhas de conexão).

---

### Text-to-Speech e Voz Personalizada

1. **Síntese de Voz na Interface Web**  
   - No Speech Studio, selecione “Text-to-Speech” → “Synthesize”.  
   - Escolha uma voz padrão (por exemplo, “pt-BR-AntonioNeural”).  
   - Digite um texto de exemplo (“Olá, este é um teste de síntese de voz com Azure”).  
   - Baixe o arquivo de áudio gerado (`tts-sample.wav`) e coloque em `/speech-studio/tts-sample.wav`.

2. **Exemplo via Código (Python)**  
   - Arquivo `text-to-speech.py`:  
     \`\`\`python  
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
     \`\`\`  
   - Documente: como trocar vozes, ajustar parâmetros (pitch, rate) via `SpeechSynthesisVoiceName` ou `SpeechSynthesisOutputFormat`.

3. **Custom Voice (opcional, se decidir aprofundar)**  
   - Explique o fluxo breve:  
     1. Coletar 15–20 gravações de voz para treino.  
     2. Fazer upload dos arquivos WAV e transcrições (.txt).  
     3. Treinar o modelo customizado no Speech Studio.  
     4. Implantar e testar a nova “Voice Font”.  
   - Inclua capturas de tela do processo de importação e treinamento no portal.  
   - Se tiver scripts PowerShell ou CLI usados para automatizar a criação de Voice Font, armazene em `/speech-studio/custom-voice-scripts/criar-voicefont.ps1`.

---

### Análise de Texto com Language Studio

1. **Sentiment Analysis na Interface Web**  
   - Acesse https://language.microsoft.com/.  
   - Na seção “Text Analytics” → “Sentiment Analysis”.  
   - Cole alguns parágrafos de exemplo em português ou inglês.  
     ![language-studio-dashboard.png](images/language-studio-dashboard.png)  
   - Observe a resposta JSON (pontuação de sentimento por frase).  
   - Salve o payload em `/language-studio/sentiment-analysis-sample.json`.

2. **Key Phrases & Entity Recognition**  
   - Ainda no Language Studio, selecione “Key Phrase Extraction”.  
     - Cole texto de exemplo → obtenha lista de palavras-chave.  
     - Salve em `/language-studio/keyphrases-sample.txt`.  
   - Selecione “Named Entity Recognition” (NER).  
     - Use texto que contenha nomes de pessoas, lugares, organizações.  
     - Copie o resultado em `/language-studio/entities-sample.json`.

3. **Exemplos de Código (Python)**  
   - Arquivo `language-analysis.py`:  
     \`\`\`python  
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
     \`\`\`  
   - Documente no README:  
     - Como configurar as credenciais (environment variables).  
     - Como interpretar cada resposta (ex.: `confidence_scores`, categorias NER).

---

## 3. Documentando Insigths e Boas Práticas

Em cada seção acima, insira anotações sobre:
- **Dificuldades encontradas**:  
  - Ex.: “A primeira tentativa de reconhecimento gerou ruído porque o arquivo de áudio não estava no formato correto (deveria ser WAV, 16 kHz PCM).”  
  - “No Text-to-Speech, descobri que algumas vozes são compatíveis apenas com determinados idiomas/regiões—tive que mudar `pt-BR-FernandaNeural` para `pt-BR-AntonioNeural`.”
- **Soluções aplicadas**:  
  - “Convertemos o áudio de `.mp3` para `.wav` usando `ffmpeg -i input.mp3 -ar 16000 output.wav`.”  
  - “Para obter frases completas na resposta de análise de sentimento, ajustamos o parâmetro `include_opinion_mining=True` (caso use o SDK).”
- **Recomendações**:  
  - “Para textos maiores que 5.120 caracteres, o Language Studio exige batch splitting—é importante dividir o texto em blocos antes de chamar a API.”  
  - “Para transcrição contínua (speech-to-text em streaming), usar `start_continuous_recognition()` em vez de `recognize_once()`.”

---

## 4. Capturas de Tela (Opcional, mas recomendável)

- Crie a pasta `/images` e organize os arquivos com nomes descritivos:  
  - **speech-studio-setup.png**: configuração inicial do Speech Studio.  
  - **language-studio-dashboard.png**: painel principal do Language Studio.  
  - **transcript-resultado.png**: resultado da transcrição.  
  - **code-snippet-analysis.png**: trecho de código executando análise de texto.

No `README.md`, insira referências às imagens:

```markdown
### Exemplo de Transcrição

![Transcrição de Áudio no Speech Studio](images/transcript-resultado.png)

### Dashboard do Language Studio

![Painel Principal do Language Studio](images/language-studio-dashboard.png)
```

---

## 5. Boas Práticas de Documentação Técnica

1. **Clareza e Objetividade**  
   - Explique cada comando, cada parâmetro naquele script ou configuração, como se falasse para um colega que nunca viu o Azure antes.  
   - Use subtítulos (“Configuração”, “Exemplo de Código”, “Observações”) para separar tópicos.

2. **Markdown bem-formatado**  
   - Use listas ordenadas (`1.`, `2.`, `3.`) para passos sequenciais.  
   - Use listas não ordenadas (`-`, `*`) para comentários paralelos ou dicas.  
   - Destaque comandos em blocos de código (```bash``` ou ```python```) para facilitar a cópia.

3. **Referências e Links**  
   - Ao mencionar a documentação oficial:  
     - `[Documentação Speech-to-Text](https://learn.microsoft.com/azure/cognitive-services/speech-service/)`  
     - `[Documentação Language Studio](https://learn.microsoft.com/azure/cognitive-services/language-service/)`  
   - Se usar SDKs, inclua link para o repositório oficial ou páginas PyPI/NuGet.

4. **Versionamento**  
   - Faça commits frequentes, com mensagens significativas:  
     - `git commit -m "Adiciona exemplo básico de speech-to-text em Python"`  
     - `git commit -m "Insere capturas de tela do Language Studio"`  
   - Na descrição do pull request (caso valide internamente), explique resumidamente o que foi documentado.

5. **Organização de Pastas**  
   - Mantenha todos os scripts de exemplo juntos em `/speech-studio` e `/language-studio`.  
   - Coloque testes ou pequenos arquivos de áudio/texto nesses diretórios para facilitar replicação pelos revisores.

---

## 6. Entrega do Projeto

1. **Validar o Repositório**  
   - Confira se o `README.md` está completo, sem tópicos em aberto.  
   - Garanta que toda imagem referenciada existe em `/images`.  
   - Verifique se os códigos têm comentários mínimos que facilitem o entendimento.

2. **Link para Entrega**  
   - No botão “Entregar Projeto” (na plataforma de aprendizagem), cole o link público do repositório, por exemplo:  
     ```
     https://github.com/seu-usuario/azure-speech-language-lab
     ```  
   - Insira uma breve descrição (duas ou três linhas) destacando:  
     - O que foi implementado/experimentado.  
     - Principais insights (ex.: “Documentei passo a passo a transcrição de áudios e análises de sentimento, identificando como lidar com limites de caracteres no Language Studio.”).

3. **Considerações Finais**  
   - Caso tenha ido além (por exemplo, criado Voice Font customizada ou integrado ambos os serviços em um fluxo automatizado), descreva resumidamente esses avanços no campo de “Próximos Passos / Recomendações”.

---

## 7. Exemplos de Arquivos

- **speech-to-text.py** (em `/speech-studio`):
```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<SPEECH_KEY>", region="<REGIÃO>")
audio_input = speechsdk.AudioConfig(filename="audio-sample.wav")
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
result = recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Transcrição:", result.text)
else:
    print("Falha:", result.reason)
```

- **text-to-speech.py** (em `/speech-studio`):
```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<SPEECH_KEY>", region="<REGIÃO>")
audio_config = speechsdk.audio.AudioOutputConfig(filename="tts-sample.wav")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

texto = "Este é um exemplo de síntese de voz via Python."
result = synthesizer.speak_text_async(texto).get()
```

- **language-analysis.py** (em `/language-studio`):
```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(endpoint="<ENDPOINT>", credential=AzureKeyCredential("<KEY>"))

docs = ["Texto exemplo para análise de sentimento.", "Outro texto para extração de frases-chave."]

# Sentimento
resp_sent = client.analyze_sentiment(documents=docs)
for doc in resp_sent:
    print(doc.sentiment, doc.confidence_scores)

# Extração de Phrases
resp_phrases = client.extract_key_phrases(documents=docs)
for doc in resp_phrases:
    print(doc.key_phrases)
```

---

## 8. Referências Úteis

- [Documentação Speech Studio](https://learn.microsoft.com/azure/cognitive-services/speech-service/)  
- [Documentação Language Studio](https://learn.microsoft.com/azure/cognitive-services/language-service/)  
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)  
