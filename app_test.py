from flask import Flask, request
from message_sandeco import MessageSandeco as Message
from send_sandeco import SendSandeco
from dotenv import load_dotenv

from fluxo_audio import FluxoAudio  # Supondo que FluxoAudio ainda é necessário

load_dotenv()

app = Flask(__name__)

@app.route("/messages-upsert", methods=['POST'])
def webhook():
    send = SendSandeco()
    
    try:
        data = request.get_json()
        msg = Message(data)     
        
        if msg.phone == "5521981388583" or "5521979047667":  # Somente Pedro e PH podem requisitar   
        
            if msg.message_type == Message.TYPE_TEXT:
                text = msg.get_text()
                
                fluxo = FluxoAudio()
                resposta = fluxo.kickoff(inputs={'text': text})  # Obtém resposta da LLM
                
                send.textMessage(number=msg.phone, msg=resposta)  # Envia resposta como texto

    except Exception as e:
        print(f"Erro ocorrido: {e}")
        send.textMessage(number=msg.phone, msg="Ocorreu um erro ao processar a mensagem. Por favor, tente novamente.")

    return "resposta"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
