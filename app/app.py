import os
import openai
import asyncio
import gspread
from db import GoogleSheetsManager
from gspread_asyncio import AsyncioGspreadClientManager
from flask import Flask, jsonify, request, render_template_string, render_template


app = Flask(__name__)

openai.api_key = os.getenv('open_ai_key')

credentials_path = './google_credentials/flaskproject-422318-b98fc950e1ed.json'
spreadsheet_id = "1OWy5An7OEDTT4aESHZdDa8x9SMDdQnEKaB6-h6Wf-8w"

sheet_manager = GoogleSheetsManager(credentials_path, spreadsheet_id)

@app.route('/', methods=['GET'])
async def index():
    await sheet_manager.read_from_sheet(1)
    return render_template('index_async.html')

@app.route('/submit', methods=['POST'])
async def submit():
    data = request.get_json()
    user_input = data.get('user_input', '')

    if user_input:
        await sheet_manager.save_to_sheet([user_input])
        
        # Get response to Prompt 1
        response_prompt1 = await get_chatgpt_response(user_input + "\n Give me 3 main problems which my product is solving.")
        await sheet_manager.save_to_sheet([response_prompt1])

        # Get response to Prompt 2
        try:
            response_prompt2 = await get_chatgpt_response(response_prompt1 + "\nPrompt 2: Based on them, write 3 advertisements for Facebook. Add some emojies.")
            await sheet_manager.save_to_sheet([response_prompt2])
            return jsonify({'response': response_prompt2})    
        except Exception as e:
            #response_prompt2 = f"An error occured, please try again later"
            return jsonify({'response': "An error occured, please try again later"})    
    else:
        # Handle empty input case
        return "Please provide input.", 400


async def get_chatgpt_response(prompt):
    # Call to OpenAI API to get a response based on user input
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": ""},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app.run(host='0.0.0.0', debug=True)
