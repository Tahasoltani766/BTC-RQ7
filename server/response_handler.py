from gpu_models import data
from fuzzywuzzy import fuzz

gpu_similar = []
for item in data:
    name = item['name'].lower()
    if 'nvidia' in name:
        gpu_similar.append(item)

data = ('NVIDIA GeForce RTX 3050 Laptop GPU').lower()

similarity_scores = [(string, fuzz.token_set_ratio(data, string)) for string in gpu_similar]
sorted_similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
most_similar_string, similarity_score = sorted_similarity_scores[0]
algorithms = most_similar_string['algorithm']
if len(algorithms) > 1:
    first_dict = None
    print(algorithms)
    for key in algorithms:
        first_dict = algorithms[key]
        print(first_dict)