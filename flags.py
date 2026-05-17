import requests
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def certificate(url):
    try:
        response = requests.get(url)
    except requests.exceptions.SSLError as s:
        print(F"bad ssl: {s}")
    except requests.exceptions.ConnectionError as c:
        print(f"connection error: {c}")

def HTLM(url,score):
    try:
        response = requests.get(url)

        if response.history:
            score += 5
            print("[!] there was a redirection")
            for redirect in response.history:
                print(redirect.status_code, redirect.url)

            print("End:", response.status_code, response.url)
        else:
                print(response.status_code)
                print(response.text)
    except requests.exceptions.RequestException as s:
        print(f"error: {s}")



def report(results):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate("report.pdf", pagesize=A4)

    contenido = []

    contenido.append(Paragraph("Educational report", styles["Title"]))
    contenido.append(Spacer(1, 10))

    for find in results:

        if "words" in find:
            contenido.append(Paragraph("Suspicious words detected", styles["Heading2"]))

            contenido.append(
                Paragraph(
                    "Words like 'secure', 'verify', 'login' and others "
                    "are commonly used to create pressure and make "
                    "the URL seem more legitimate to the victim.",
                    styles["BodyText"]
                )
            )

            contenido.append(Spacer(1, 10))

        if "ipv4" in find:
            contenido.append(Paragraph("IPv4 detected in the URL", styles["Heading2"]))

            contenido.append(
                Paragraph(
                    "Using an IPv4 address in a URL may indicate phishing, "
                    "as it avoids domain registration and can hide identity.",
                    styles["BodyText"]
                )
            )

            contenido.append(Spacer(1, 10))

        if "long_domain" in find:
            contenido.append(Paragraph("Very long domain detected", styles["Heading2"]))

            contenido.append(
                Paragraph(
                    "Very long URLs are often used to confuse users "
                    "and hide suspicious parts of the address.",
                    styles["BodyText"]
                )
            )

            contenido.append(Spacer(1, 10))

        if "http" in find:
            contenido.append(Paragraph("HTTP protocol detected", styles["Heading2"]))

            contenido.append(
                Paragraph(
                    "The URL uses HTTP instead of HTTPS. "
                    "This means the connection is not encrypted "
                    "and may be unsafe.",
                    styles["BodyText"]
                )
            )

            contenido.append(Spacer(1, 10))

        if "shortener" in find:

            contenido.append(Paragraph("URL shortener detected", styles["Heading2"]))

            contenido.append(
                Paragraph(
                    "Shortened URLs can hide the real destination "
                    "and are frequently used in phishing campaigns.",
                    styles["BodyText"]
                )
            )

            contenido.append(Spacer(1, 10))

        if "subdomain" in find:

            contenido.append(Paragraph("too many subdomains", styles["Heading2"]))

            contenido.append(
                Paragraph(
                    "too many subdomain could be suspicious for hide the real domain and appear legitimate ",
                    styles["BodyText"]
                )
            )

            contenido.append(Spacer(1, 10))

    contenido.append(
        Paragraph(
            "Note: sometimes phishing URLs in the real world "
            "tend to be more sophisticated. "
            "This report is for educational and experimental purposes only.",
            styles["Italic"]
        )
    )

    doc.build(contenido)


