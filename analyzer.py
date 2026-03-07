import re
import tldextract
from flags import HTLM
from flags import certificate
from scoring import score

def analyzer(URL,H,ss):

    sign = 0
    total_score = 0
    suspicious_words = ["secure","verify","account","bank","login","update"]
    found = []

    try:

        count_guion = URL.count("-")
        count_characters = len(tldextract.extract(URL).domain)
        ext = tldextract.extract(URL).subdomain
        domain = tldextract.extract(URL).registered_domain

        pattern = f"https?://({domain})/[a-zA-Z0-9]+"
        patternIp4 = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b'

        for word in suspicious_words:
            if word in URL:
                found.append(word)
                total_score += 5
                sign += 1
        print(f"[*] suspicous words detected: {found}")

        if ext:
            lista_subdominios = ext.split('.')
            count_subdomain = len(lista_subdominios)

            if count_subdomain >= 4:
                total_score += 5 
                sign += 1 
                print(f"[!] too much subdomains: {count_subdomain}")

        if count_characters >= 25:
            total_score += 5
            sign += 1
            print(f"[!] domain very long: {count_characters} domain: {domain}") 

        if count_guion >= 4:
                total_score += 5
                sign += 1
                print(f"[!] too much - {count_guion}")  

        if re.search(patternIp4, URL):
            total_score += 15
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

        if ss:
            certificate(URL)

        if H:
            HTLM(URL,total_score)
            
        score(sign,total_score)

    except Exception as r:
        print(r)

       