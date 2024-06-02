from keyword_research import generate_keyword_ideas
from multilingual import translate_text
import csv, os

base_language = "English"

languages = ["Tamil", "Bengali", "Hindi", "Malayalam", "Marathi", "Kannada", "Gujarati", "Telugu", "Punjabi"]


conditions = ['Bariatric Surgery', 'Neuro ophthalmic Disorders', 'Vaginal Cyst', 'female infertility', 'Diabetic retinopathy', 'Total Hip Replacement Surgery']

seed_keywords = ['surgery_name language', 'surgery_name benefits in language', 'surgery_name side effects in language', 'surgery_name meaning in language']

language_seed_keywords = ['surgery_name', 'surgery_name benefits', 'surgery_name side effects', 'surgery_name meaning']


def read_nth_column_csv(file_path, n):
    column_data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > n:
                column_data.append(row[n])
    return column_data

def save_to_csv(file_path, surgery, language, keywords_ideas):
    with open(file_path, mode='a', newline='') as file:
        fieldnames = ['surgery', 'language', 'keywords_list', 'keywords_volumes_list', 'total_volume']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Concatenate keywords and volumes into single strings
        keywords_list = "\n".join([data['keyword'] for data in keywords_ideas])
        keywords_volumes_list = "\n".join([f"{data['keyword']} - {data['volume']}" for data in keywords_ideas])
        total_volume = sum([data['volume'] for data in keywords_ideas])
        
        # Create a dictionary for the row
        row = {
            'surgery': surgery,
            'language': language,
            'keywords_list': keywords_list,
            'keywords_volumes_list': keywords_volumes_list,
            'total_volume': total_volume
        }
        
        # Write the row to the CSV file
        writer.writerow(row)

def initialize_csv(file_path):
    # Open the file in write mode to clear existing content and write the header
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['surgery', 'language', 'keywords_list', 'keywords_volumes_list', 'total_volume']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()     

file_path = 'language+surgery.csv'
surgeries = read_nth_column_csv(file_path,1)
response = 'response.csv'
initialize_csv(response)

seed_keys = ['surgery language', 'surgery Symptoms language', 'surgery causes language', 'surgery risks language', 'surgery meaning language', 'surgery treatment language']

for surgery in surgeries:
    surgery = surgery.lower()
    for language in languages:
#         # translated_lan = translate_text(condition, base_language, language)
#         # print (translated_lan)
        
        # generating the keyword list
        language = language.lower()
        k_seed_keywords = [seed_key.replace('surgery', surgery).replace('language', language)  for seed_key in seed_keys]
        # print (k_seed_keywords)
        keywords_ideas = generate_keyword_ideas(k_seed_keywords)
        # print(keywords_ideas[:5])
        save_to_csv(response, surgery, language, keywords_ideas)


