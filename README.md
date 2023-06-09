# Chatbot-Django

This project is a chatbot built using the Django web framework in Python, which uses OpenAI's API to perform data analysis on user messages. The goal of the project is to provide users with a conversational interface that can answer questions, provide recommendations, and analyze data based on the user's input.

## Dependencies
The project requires the following dependencies:

- Python 3.6 or higher
- Django 3.1 or higher
- OpenAI API key

## Installation
To install the project, follow these steps:

1. Clone the repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/KumailQazi/Chatbot-Django.git
2. Install the project dependencies using pip:

bash
Copy code
pip install -r requirements.txt
3. Create a .env file in the project root directory with the following contents:

bash
Copy code
OPENAI_API_KEY=your-api-key-here

Replace your-api-key-here with your actual OpenAI API key.

4. Run the Django development server:

bash
Copy code
python manage.py runserver

You should now be able to access the chatbot interface by visiting http://localhost:8000/chat/ in your web browser.

## Usage
To use the chatbot, simply enter a message in the chat input box and press the "Send" button. The chatbot will analyze your message using OpenAI's API and provide a response based on the analysis.

## Contributing
If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository and create a new branch for your changes.

2. Make your changes and write unit tests to ensure that your changes work as expected.

3. Push your changes to your fork and create a pull request to the main repository.

4. The project maintainer will review your changes and provide feedback.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.