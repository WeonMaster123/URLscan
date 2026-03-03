# URLscan 
URLscan is an educational project rule based about basic phishing detection techniques in a url. This software is not intended for use in real-world environments.
It was created for learning and experimentation purposes only.

# Can detect:
- too much - or subdomains
- IPv4 in the domain
- very long domain
- Whether or not it uses http.
- shortener in the url

example:
<img width="1657" height="171" alt="detected" src="https://github.com/user-attachments/assets/89c75c5f-948e-41f6-895a-9e5b637c5b94" />

# How to use 
```bash
python3 urlscan.py https://your-url-suspicious.com [flags]
```

# Flags and system score
For now, this project includes two optional flags:

-H → Retrieves and analyzes the HTML content of the page.

-ss → Verifies the SSL certificate. If the certificate is invalid (for example, expired), the program returns an error.

The scoring system increases the risk score whenever a rule matches. Based on the final score, the URL is classified as: 
- possible low risk
- possible medium risk
- possible high risk. 

The final score is also displayed.

# Limitations
This project does not detect:
- domain age
- domain reputation
- suspicious words
- typosquatting or similar techniques 
- WHOIS data

example:
<img width="1657" height="171" alt="no_detected" src="https://github.com/user-attachments/assets/2b69ca54-44f6-4c3d-ab99-4a33821fff05" />

# Installation
Make sure you have Python 3 installed. Then install dependencies:

```bash
pip install requests tldextract
```

# License
This project is licensed under the MIT License.

