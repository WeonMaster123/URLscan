# PhishSCAN 
PhishSCAN is an educational project rule based about basic phishing detection techniques in a url. This software is not intended for use in real-world environments.
It was created for learning and experimentation purposes only.

# Can detect:
- too much - or subdomains
- IPv4 in the domain
- very long domain
- Whether or not it uses http.
- shortener in the url
- some suspicious words

example:
<img width="1850" height="177" alt="detected" src="https://github.com/user-attachments/assets/3b2cf3aa-2ef5-4108-b48a-5fd31d3d4298" />

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
- other suspicious words
- typosquatting or similar techniques 
- WHOIS data

example:
<img width="1850" height="177" alt="not_detected" src="https://github.com/user-attachments/assets/c701e91c-cc69-45f7-87b1-2e0e62d98458" />


# Installation
Make sure you have Python 3 installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

# License
This project is licensed under the MIT License.

