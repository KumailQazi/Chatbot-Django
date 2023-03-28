# Uses pandas to describe data
from django.http import JsonResponse
import openai
import os
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
import csv
import io
import pandas as pd

# Set up the OpenAI API key

api_key_path = os.path.abspath("../build/Okey.txt")
with open(api_key_path, "r") as f:
    api_key = f.read().strip()

openai.api_key = api_key

# Define the prompt for the chatbot
prompt = "Hello, how can I help you today?"

# Define a function to generate a response from the chatbot
# Define a function to generate a response from the chatbot
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        stop=None,
        n=1,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1
    )
    return response.choices[0].text.strip()


@csrf_exempt
def chat(request):
    global prompt
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES['file']
            # Read the uploaded file using Pandas
            data = pd.read_csv(io.StringIO(file.read().decode('utf-8')))
            # description = data.describe().to_string()
            description = data.describe().to_html()
            # Perform analysis on the data here...
            # ...
            # response = "Analysis complete!"
            response = f"Here's a summary of the data: \n\n{description}"
        else:
            message = request.POST.get('message')
            global prompt
            prompt += f"\nUser: {message}\nAI:"
            response = generate_response(prompt)
            prompt += f"{response}\n"
        return JsonResponse({'response': response})
    else:
        prompt = "Hello, how can I help you today?"  # Initialize the prompt variable
        return render(request, 'chat.html', {'prompt': prompt})
        # return render(request, 'chat.html')