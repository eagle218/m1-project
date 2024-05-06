# Launch the application

To launch the application, follow these steps:

## 1. Installing dependencies

Make sure you have Python version 3.x installed. Then install the dependencies listed in the requirements.txt file by running the following command:
pip install -r requirements.txt

## 2. Obtaining Google Credentials

You must have a JSON file with Google credentials to access the Google Sheets. Specify the path to this file in the `credentials_path` variable in your application code.

## 3. Specifying Spreadsheet ID

Specify the Google Sheets spreadsheet ID (spreadsheet_id) you want to access in the `spreadsheet_id` variable in your application code.

## 4. Launching the application

Once you've installed the dependencies, specified the Google Credentials file path, and the Google Sheets table ID, you can run the application by running the following command:
python app.py


The application will be launched at http://localhost:5000/.

## 5. Using the application

After launching the application, you can open your browser and go to http://localhost:5000/ to access the main page. You can also send POST requests to http://localhost:5000/submit with data in JSON format to receive responses from OpenAI and save them in Google Sheets.
