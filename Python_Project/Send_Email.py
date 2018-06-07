import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

def Send_Text():
    message = EmailMessage()
    message['Subject'] = '안녕하세요ㅎㅎ !!'
    message['From'] = 'skspah888@naver.com'
    message['To'] = 'sj9913@hanmail.net'
    message.set_content('고생많으십니다 ㅋㅋ..')

    with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
        server.ehlo()
        server.login('skspah888', 'wnsroaht153!')
        server.send_message(message)
    print("텍스트 이메일을 발송하였습니다")

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
    print("HTML 이메일을 발송하였습니다")



