import re
import sys
import os
from rapidfuzz import fuzz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.helpers import load_data

data_csv = load_data("data/ICDCodeSet.csv")
# print(data_csv.head())
def normalize_symptoms(user_input):
    normalized = []
    user_input_lower = user_input.lower()
    debug_limit = 10
    debug_count = 0

    user_input_clean = re.sub(r'[^a-zA-Z0-9\s]', '', user_input.lower())
    keywords = [word.strip().lower() for word in user_input_clean.split() if len(word) > 3]

    for _, row in data_csv.iterrows():
        description = str(row['Description']).lower()

        description_clean =  re.sub(r'[^a-zA-Z0-9\s]', '', description)
        #using token sort ratio  instead of partial ratio
        # score = fuzz.partial_ratio(user_input_lower, description)
        for keyword in keywords:
            score = fuzz.token_sort_ratio(keyword, description_clean)

            if score >= 80:
                print(f"mathced ({score}%): {description}")
                normalized.append((row['Description'], row['ICDCode']))
                
            elif debug_count < debug_limit:
                print(f"NOT {description} - score: {score}%")

                debug_count += 1

        # if str(row['Description']).lower() in user_input.lower():
        #     # print()
        #     normalized.append((row['Description'], row['ICDCode']))
        # else:
        #     print("yo")
    return normalized

result = normalize_symptoms("I think I have typhoid fever or maybe some salmonella")
# for i, j in result:
#     print(f"{i} -> {j}")

