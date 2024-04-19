#!/usr/bin/env python3

import os
import sys
import google.generativeai as genai

def configure_api_key():
    # Check if API key is provided as command-line argument
    if len(sys.argv) > 1:
        return sys.argv[1]
    
    # Check if API key is set in environment variable
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key:
        return api_key
    
    # Prompt user to enter API key if not found
    return input("Enter your Google API key: ")

def main():
    # Configure GenerativeAI API key
    api_key = configure_api_key()
    genai.configure(api_key=api_key)

    # Initialize GenerativeModel and start chatting
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    try:
        while True:
            # Prompt user for input
            prompt = input("Ask me anything: ")

            # Check if user wants to exit
            if prompt.lower() == "exit":
                break

            # Send user input to GenerativeAI model
            response = chat.send_message(prompt, stream=True)

            # Process response
            if response is not None:
                for chunk in response:
                    if hasattr(chunk, 'text'):
                        print(chunk.text)
                    else:
                        print("Response does not contain valid text.")
            else:
                print("No response received.")

    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
