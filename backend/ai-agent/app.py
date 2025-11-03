from flask import Flask, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",  # change to gemini-1.5-flash if needed
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="""You are an expert at teaching science to kids. Your task is to engage in 
                          conversations about science and answer questions. Explain scientific concepts 
                          so that they are easily understandable. Use analogies and examples that are 
                          relatable. Use humor and make the conversation both educational and interesting. 
                          Ask questions so that you can better understand the user and improve the 
                          educational experience. Suggest ways that these concepts can be related to the 
                          real world with observations and experiments.""",
)

@app.route('/AIResponse', methods=['POST'])
def ai_response():
    data = request.get_json()
    user_input = data.get('user_input') if data else None

    if not user_input:
        return jsonify({"error": "Missing 'user_input' field"}), 400

    # Start a new chat for each request
    chat_session = model.start_chat(history=[])

    try:
        response = chat_session.send_message(user_input)
        model_response = response.text
        return jsonify({
            'user_input': user_input,
            'bot_message': model_response
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1213, debug=False)
