import re
from scoring import scor

def analyzer(URL):
    found = []
    score = 0

    texto = "http://"

    shorteners = r"bit\.ly|tinyurl\.com|goo\.su|t\.co"
    Pattern = f"https?://({shorteners})/[a-zA-Z0-9]+"
    if re.findall(Pattern, URL):
        print("[!] shorteners in the url")        
        score += 10
        found.append("shorteners")

    if texto in URL:
        print("[!] http in the url")
        score += 5
        found.append("http")

    scor(found,score)