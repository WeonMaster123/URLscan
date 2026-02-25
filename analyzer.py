import re
import requests
import tldextract
from scoring import score

def analyzer(URL,H):

    sign = 0
    total_score = 0

    count_guion = URL.count("-")
    count_characters = len(tldextract.extract(URL).domain)

    shorteners = r"bit\.ly|tinyurl\.com|goo\.su|t\.co"
    pattern = f"https?://({shorteners})/[a-zA-Z0-9]+"
    patternIp4 = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b'

    if count_characters >= 25:
        total_score += 5
        sign += 1
        print(f"[!] too much characters: {count_characters}") 

    if count_guion >= 4:
            total_score += 5
            sign += 1
            print(f"[!] too much - : {count_guion}")  

    if re.search(patternIp4, URL):
        total_score += 10
        sign += 1
        print("[!] detected ip4")

    if re.findall(pattern, URL):        
        total_score += 15
        sign += 1
        print("[!] shortener in the url")

    if "http://" in URL:
        total_score += 10
        sign += 1
        print("[!] http in the url")
    
    if H:
        response = requests.get(URL)
        print(response.text)
        print(f"[*] status code: {response.status_code}") 
        

    score(sign,total_score)
