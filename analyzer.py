import re
import tldextract
from flags import HTLM
from flags import certificate
from flags import report
from scoring import score

def analyzer(URL,H,ss,r):

    sign = 0
    total_score = 0
    suspicious_words = ["secure","verify","account","bank","login","update"]
    suspicious_found = []
    found = set()

    try:

        count_guion = URL.count("-")
        count_characters = len(tldextract.extract(URL).domain)
        ext = tldextract.extract(URL).subdomain
        domain = tldextract.extract(URL).registered_domain

        pattern = f"https?://({domain})/[a-zA-Z0-9]+"
        patternIp4 = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b'

        for word in suspicious_words:
            if word in URL:
                suspicious_found.append(word)
                total_score += 5
                sign += 1
                found.add("words")
        print(f"[*] suspicous words detected: {suspicious_found}")

        if ext:
            lista_subdominios = ext.split('.')
            count_subdomain = len(lista_subdominios)

            if count_subdomain >= 4:
                found.add("subdomain")
                total_score += 5 
                sign += 1 
                print(f"[!] too much subdomains: {count_subdomain}")

        if count_characters >= 25:
            found.add("long_domain")
            total_score += 5
            sign += 1
            print(f"[!] domain very long: {count_characters} domain: {domain}") 

        if count_guion >= 4:
                found.add("-")
                total_score += 5
                sign += 1
                print(f"[!] too much - {count_guion}")  

        if re.search(patternIp4, URL):
            found.add("ipv4")
            total_score += 15
            sign += 1
            print("[!] detected ip4")

        if re.findall(pattern, URL):
            found.add("shortener")       
            total_score += 15
            sign += 1
            print("[!] shortener in the url")

        if "http://" in URL:
            found.add("http")
            total_score += 10
            sign += 1
            print("[!] http in the url")

        
        if ss:
            certificate(URL)

        if H:
            HTLM(URL,total_score)
        if r:
            report(found)
            print("[*] created report")
            
        score(sign,total_score)

    except Exception as r:
        print(r)
       