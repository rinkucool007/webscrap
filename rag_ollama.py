import requests
import os

def query_ollama(query, html_filepath):
    url = "http://127.0.0.1:11434/llama3.2"
    with open(html_filepath, 'r', encoding='utf-8') as file:
        html_content = file.read()

    payload = {
        "query": query,
        "context": html_content
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    try:
        response_data = response.json()
        print(f"Response JSON: {response_data}")  # Debug: print the response
        return response_data["result"]
    except ValueError as e:
        print(f"JSON decoding failed: {e}")
        print(f"Response Text: {response.text}")  # Debug: print the raw response text
        return []
