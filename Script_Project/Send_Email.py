import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

def Send_Text(word,Dict):
    message = EmailMessage()
    message['Subject'] = ''' "맛집을 찾아라!!" 즐겨찾기 리스트 입니다!!! '''
    message['From'] = 'skspah888@naver.com'
    message['To'] = str(word)

    message.set_content(str(Dict.items()).replace('dict_items',""))

    with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
        server.ehlo()
        server.login('skspah888', 'wnsroaht153!')
        server.send_message(message)

def Send_File():
    pass

def Send_HTML():
    message = EmailMessage()
    message['Subject'] = '안녕하세요ㅎㅎ !!'
    message['From'] = 'skspah888@naver.com'
    message['To'] = 'skspah888@naver.com'
    message.add_alternative('''
    <h1>VOD</h1>
    <ul>
    <li>크롤링 시작하기</li>
    <li>파이썬으로 업무 자동화</li>
    </ul>
    
    ''',subtype='html')

    with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
        server.ehlo()
        server.login('skspah888', 'wnsroaht153!')
        server.send_message(message)




