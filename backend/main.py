import os
import uuid
import requests
from flask import Flask, render_template, request, jsonify
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# O index.html fica na pasta frontend, um nível acima deste arquivo.
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(project_dir, "frontend")
app = Flask(__name__, template_folder=template_dir)

# --- CONFIGURAÇÕES DO WATSON ASSISTANT ---
API_KEY = os.getenv("WATSON_API_KEY", "KEBT6SoMU8BbsLnATvKw9uEUaqoEm1O9m3EEuEt7fh_z")
ASSISTANT_ID = os.getenv("WATSON_ASSISTANT_ID", "93eda45a-1df5-4735-aa5d-9e3ca3b27b47")
SERVICE_URL = os.getenv("WATSON_URL", "https://api.us-south.assistant.watson.cloud.ibm.com")
ENVIRONMENT_ID = os.getenv("WATSON_ENVIRONMENT_ID", "93eda45a-1df5-4735-aa5d-9e3ca3b27b47")

# Autenticação com a SDK da IBM
authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)
assistant.set_service_url(SERVICE_URL)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    user_message = data.get("message", "")
    context = data.get("context", {})

    try:
        session_id = context.pop("session_id", None)
        user_id = context.pop("user_id", None) or str(uuid.uuid4())
        if not session_id:
            token = authenticator.token_manager.get_token()
            session_url = (
                f"{SERVICE_URL}/v2/assistants/{ASSISTANT_ID}"
                f"/environments/{ENVIRONMENT_ID}/sessions"
            )
            session_response = requests.post(
                session_url,
                params={"version": "2021-11-27"},
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                },
                json={"user_id": user_id},
                timeout=30
            )
            session_response.raise_for_status()
            session_id = session_response.json()["session_id"]

        response = assistant.message(
            assistant_id=ASSISTANT_ID,
            environment_id=ENVIRONMENT_ID,
            session_id=session_id,
            input={'message_type': 'text', 'text': user_message},
            context={'global': context},
            user_id=user_id
        ).get_result()

        # Extrai os textos retornados pelos dialog_nodes
        generic_responses = response.get('output', {}).get('generic', [])
        bot_messages = []

        for resp in generic_responses:
            if resp.get('response_type') == 'text' and resp.get('text'):
                bot_messages.append(resp.get('text'))

        # Fallback de segurança se o nó não retornar array genérico
        if not bot_messages and 'text' in response.get('output', {}):
            bot_messages = response['output']['text']

        response_context = response.get("context", {}).get("global", {})
        response_context["session_id"] = session_id
        response_context["user_id"] = user_id

        return jsonify({
            "status": "success",
            "context": response_context,
            "response": bot_messages if bot_messages else ["Não compreendi. Pode reformular?"]
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, port=5000)