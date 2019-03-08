import json
import re
recipes = tuple(open("f:\\recipe.json", 'r'))
result = list()

for recipe in recipes:
    JSON = json.loads(recipe)
    Result = len(re.findall(r"[Cc]{1}h[ie]{1,3}[l]{1,2}[ie]{1,3}[s]{0,1}", JSON["ingredients"]))
    if Result:
        JSON["status"] = get_status(JSON)
        result.append(JSON)
f = open("f:\\result.csv", "wt",encoding="utf-8")
keys = result[0].keys()

#Headers to CSV
for e in keys:
    f.write(e)
    f.write(";")

f.write("\n")

#Writing elements to CSV
for e in result:
    text = ""
    for k in keys:
        if k in e.keys():
            text += e[k].replace("\n", " ").replace(";" ,",") + ";"
        else:
            text += "Unknown;"
    f.write(text + "\n")
f.close()

def get_status(JSON):
    status = ""

    #If chilie was foud, initiating time parsing
    CTH = re.findall(r"[0-9]+H", JSON["cookTime"])
    CTM = re.findall(r"[0-9]+M", JSON["cookTime"])
    PTH = re.findall(r"[0-9]+H", JSON["prepTime"])
    PTM = re.findall(r"[0-9]+M", JSON["prepTime"])

    minutes = -1

    #calculating time parsed in integer
    if len(CTM):
        minutes += int(CTM[0][:len(CTM[0]) - 1])
    if len(PTM):
        minutes += int(PTM[0][:len(PTM[0]) - 1])
    if len(CTH):
        minutes += int(CTH[0][:len(CTH[0]) - 1]) * 60
    if len(PTH):
        minutes += int(PTH[0][:len(PTH[0]) - 1]) * 60

    #status based on time
    if minutes > 60:
        status = "Hard"
    elif 30 <= minutes <= 60:
        status = "Medium"
    elif 0 < minutes < 30:
        status = "Easy"
    else:
        status = "Unknown"
    return status