

from flask import Flask, request
from message_types import MessageTypes as Message
from send_message import SendMessage
from generate import TextToSpeech
from transcript import Transcript
from dotenv import load_dotenv

import base64

from fluxo_audio import FluxoAudio


load_dotenv()

app = Flask(__name__)

@app.route("/messages-upsert", methods=['POST'])
def webhook():

    send = SendMessage()
    try:
        data = request.get_json()
                
        msg = Message(data)     
        
        if msg.phone == "5521981388583": #Somente Pedro pode requisitar   
        
            if msg.message_type == Message.TYPE_TEXT:
            
                text = msg.get_text()
            
            elif msg.message_type == Message.TYPE_AUDIO:
                
                tsc = Transcript()
                text = tsc.get_text(msg)
                
                                    
            fluxo = FluxoAudio()
            resposta = fluxo.kickoff(inputs={'text':text})

            speech = TextToSpeech()
            speech.synthesize_speech(text=resposta, 
                                        output_file="output.mp3")

            send = SendMessage()
            send.audio(number=msg.phone, audio_file="output.mp3")
    except Exception as e:
        print(f"Error occurred: {e}")
        send = SendMessage()
        send.text(number=msg.phone, text="Ocorreu um erro ao processar a mensagem. Por favor, tente novamente.")

    return "resposta"
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
