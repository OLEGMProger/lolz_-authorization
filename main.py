from email import header
import requests
from twocaptcha import TwoCaptcha
import re
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
df_id_pattern = re.compile(r'document\.cookie\s*=\s*"([^="]+)="\s*\+\s*toHex\(slowAES\.decrypt\(toNumbers\(\"([0-9a-f]{32})\"\)', re.MULTILINE)
solver = TwoCaptcha('YOUR_API_KEY')



headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36',
}


sess = requests.Session()
response1 = sess.post('https://lolz.guru/login', headers=headers)


soup = BeautifulSoup(response1.text, 'lxml')
script = soup.find_all('script')[1]
match = df_id_pattern.search(script.string)
cipher = AES.new(bytearray.fromhex("e9df592a0909bfa5fcff1ce7958e598b"), AES.MODE_CBC,
                    bytearray.fromhex("5d10aa76f4aed1bdf3dbb302e8863d52")
                    )


sess.cookies.set("sfwefwe",cipher.decrypt(bytearray.fromhex(match.group(2))).hex())



result = solver.recaptcha(sitekey='6LdAh8YUAAAAACraj__ZkvtB6l3ZDpa0AUNgaOLj',
                          url='https://lolz.guru/login/',
                          version="v3"
                         )



data = {
    'login': 'YOUR_LOGIN',
    'password': 'YOUR_PASS',
    'remember': '1',
    'g-recaptcha-response': result["code"],
    'googleCaptcha_type': 'recaptchaV3',
    'stopfuckingbrute1337': '1',
    'cookie_check': '1',
    '_xfToken': '',
    'redirect': 'https://lolz.guru/market/steam/',
}


sess.post('https://lolz.guru/login', headers=headers, data=data)
print(sess.cookies.get_dict())
