Free Translator Chatbot

A simple yet powerful language translator web application built using Streamlit. This project allows users to translate text into multiple languages and listen to the translated output using text-to-speech functionality.

Overview

The Free Translator Chatbot is designed to provide quick and accessible translations with an intuitive interface. It combines real-time translation with audio output, making it useful for language learners, travelers, and anyone needing instant multilingual support.

Features
Translate text into multiple languages
Automatic source language detection
Clean and interactive user interface
Text-to-speech output for translated text
Support for widely used global languages including Urdu, French, German, Spanish, Chinese, Arabic, Hindi, Turkish, Russian, Japanese, Korean, and Punjabi
Technologies Used
Python
Streamlit
deep-translator
gTTS (Google Text-to-Speech)
Installation

Follow these steps to run the project locally:

Clone the repository:
git clone https://github.com/your-username/translator-chatbot.git
Navigate to the project directory:
cd translator-chatbot
Create a virtual environment:
python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt
Running the Application

Start the Streamlit app with the following command:

streamlit run your_filename.py

Replace your_filename.py with the name of your Python file.

How It Works
The user inputs text into the application.
The system automatically detects the source language.
The selected target language is applied using deep-translator.
The translated text is displayed instantly.
The translated output is converted into speech using gTTS and played within the app.
Use Cases
Language learning and pronunciation practice
Quick translation for communication
Educational demonstrations of NLP concepts
Accessibility support through audio output
Future Improvements
Support for male and multiple voice options
Offline translation capabilities
Speech-to-text input
Improved UI/UX design
Save and download translated audio
Contributing

Contributions are welcome. If you would like to improve this project, feel free to fork the repository and submit a pull request.

License

This project is open-source and available under the MIT License.
