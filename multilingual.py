import requests
import json
import csv
import os
import random
import time



api_keys  = ["nUr3ZhTaJTIEeFaIDbCyCmr6pm_H-EdZqgmIr8Eq2omhv2ntw2ny4qHI5_HOGqkd", 
            "qoybpQ7UD4aaSLw1-frGyDr1xOkZL2rWY9eFXYUQm9WVjCgp10yr5DSL4XiNh9Ct",
            "G0xjC81Ua6v-v2XeW5uS6ZDAFKzQ2QzFmb4R0OIx85sT-p1SmGJF3dIjaz8XtlSD",
            "XQIBw2TCdtfb0jbh0132CbitQALr4uWtBiwZOx8zLH0Dh68Rsroar9R-zofdZdU_",
            "lzKNyaOY33mmIJv_bRKBuOGBHHdKObzWBWQcU7ElUoJ4jneGsh5Qxbcl7-x8J57E"]

# # Replace with your actual Inference API Key Value
api_key = "nUr3ZhTaJTIEeFaIDbCyCmr6pm_H-EdZqgmIr8Eq2omhv2ntw2ny4qHI5_HOGqkd"

# api_keys  = ["nUr3ZhTaJTIEeFaIDbCyCmr6pm_H-EdZqgmIr8Eq2omhv2ntw2ny4qHI5_HOGqkd"]


# Headers and data for the POST request
headers = {
    "Content-Type": "application/json",
    "Authorization": api_key
}


def translate_text(inputText, input_language, output_language):
    # API endpoint for translation
    url = "https://tts.bhashini.ai/v1/translate"
    
    data = {
        "inputText": inputText.strip(),
        "inputLanguage": input_language,
        "outputLanguage": output_language
    }
    
    # Making the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Checking the response
    if response.status_code == 200:
        translated_text = response.text
        print ("Input Text:", inputText)
        print("Translated Text:", translated_text)
        return translated_text
    else:
        print(f"Failed to translate text. Status Code: {response.status_code}. Response: {response.text}")
        return None

