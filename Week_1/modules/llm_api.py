import sys

sys.path.append(".")

import os
import logging
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv
from utils.utils import split_think_content

load_dotenv()

API_KEY = os.getenv('LLM_API_KEY')
API_URL = os.getenv('LLM_API_URL', 'https://api.openai.com/v1')

logging.basicConfig(level=logging.INFO)

class LLMAPI:
    def __init__(self, api_key=API_KEY, api_base=API_URL):
        self.client = OpenAI(api_key=api_key, base_url=api_base)
        # self.api_key = api_key
        # openai.api_key = api_key
        # if api_base:
        #     openai.api_base = api_base

    def generate(self, prompt, system_prompt=None, model="qwen/qwen3-32b", **kwargs):
        logging.info(f'Generating response for model: {model}')
        messages = []
        if system_prompt:
            logging.info(f'System prompt: {system_prompt}')
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        logging.info(f'Prompt: {prompt}')
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            logging.info(f'LLM response: {response.choices[0].message.content}')
            think_content, output_content = split_think_content(response.choices[0].message.content)
            return output_content
        except Exception as e:
            logging.error(f'LLM API error: {e}')
            return None


if __name__ == "__main__":
    llm = LLMAPI()
    prompt = "Draft an email to schedule a meeting."
    result = llm.generate(prompt)
    print("LLM Response:", result)