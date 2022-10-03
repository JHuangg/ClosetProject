import json

with open('data.json') as json_file:
    data = json.load(json_file)

review_list = []
for i in range(0, len(data["Results"])):
    review_list.append(data["Results"][i]["ReviewText"])

with open('reviews.txt', 'w') as f:
    for line in review_list:
        f.write(f"{line}\n")