![image](https://github.com/eagle218/m1-project/assets/113504886/efe4b8a2-d8a7-4e2b-988f-2c7bb2d61d4d)

![image](https://github.com/eagle218/m1-project/assets/113504886/c7a5218c-acb7-4da7-a1bb-b1021437304d)

# Launch the application

To launch the application, follow these steps:

## 1. Installing dependencies

Make sure you have Python version 3.x installed. Then install the dependencies listed in the requirements.txt file by running the following command:
pip install -r requirements.txt

## 2. Obtaining Google Credentials

You must have a JSON file with Google credentials to access the Google Sheets. Specify the path to this file in the `credentials_path` variable in your application code.

## 3. Specifying Spreadsheet ID

Specify the Google Sheets spreadsheet ID (spreadsheet_id) you want to access in the `spreadsheet_id` variable in your application code.

## 4.Install and use the OpenAI API key

To use an OpenAI API key in your application, you must set the `open_ai_key` environment variable containing your API key.

Obtaining an OpenAI API key

If you don't already have an OpenAI API key, you can get one from the OpenAI website. Register on [OpenAI official website](https://openai.com/) and get an API key.

Setting the environment variable

Once you have the API key, you can set the `open_ai_key` environment variable so that your application can use it. Here's how to do it:

On Linux/macOS operating system
bash:
    export open_ai_key=YOUR_API_KEY
On Windows:
    set open_ai_key=your_open_ai_key

## 4. Launching the application

Once you've installed the dependencies, specified the Google Credentials file path, and the Google Sheets table ID, you can run the application by running the following command:
python app.py


The application will be launched at http://localhost:5000/.

## 5. Using the application

After launching the application, you can open your browser and go to http://localhost:5000/ to access the main page. You can also send POST requests to http://localhost:5000/submit with data in JSON format to receive responses from OpenAI and save them in Google Sheets.
