import requests
from bs4 import BeautifulSoup

r = requests.get('http://python.beispiel.programmierenlernen.io/index.php')

r.__dict__

print(r.status_code)
print(r.headers)
#print(r.text)

html = """

    <html>
        <body>
            <p class="some">Ich bin ein Absatz</p>
            <p>Ich bin noch ein Absatz</p>
        </body>
    </html>
"""
doc = BeautifulSoup(html, features="lxml")

print(doc.find_all("p"))


