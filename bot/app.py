import json
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = ''

persona_prompt = """
Você é um assistente especializado em Scrum.
Seu nome é ScrumMasterX, e você tem o objetivo de auxiliar pessoas com dúvidas sobre a metodologia Scrum.
Você é sempre claro e educado em suas respostas, e gosta de fornecer exemplos práticos e explicações detalhadas sobre como aplicar Scrum em projetos de desenvolvimento.
Seja sempre amigável e paciente ao lidar com perguntas complexas.
Você nunca responde sobre outros assuntos que não sejam Scrum.
"""

@app.route('/scrum-assistant', methods=['POST'])
def scrum_assistant():
    data = request.json
    user_question = data.get('question')

    # Chama a API da OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ou "gpt-4" se você tiver acesso
        messages=[
            {"role": "system", "content": persona_prompt},
            {"role": "user", "content": user_question}
        ],
        max_tokens=150
    )

    # Extraindo a resposta correta do novo formato
    answer = response['choices'][0]['message']['content'].strip()

    # Retornando a resposta com os caracteres especiais decodificados corretamente
    return json.dumps({"answer": answer}, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
