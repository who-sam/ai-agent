import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    args = sys.argv[1]

    # checking for user arguments
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    # vars
    # user_prompt = " ".join(args)
    user_prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # tracking conversation
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]

    # generating response 
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages
    )

    if sys.argv[-1]=="--verbose":
        # printing output
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Response:")
        print(response.text)
    else:
        print(response.text)






if __name__ == "__main__":
    main()
