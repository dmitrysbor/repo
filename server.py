from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.parse import urlsplit

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        result=urlparse(self.requestline)
        num=result[4].split()[0]
        num=num.split('=')
        MyHandler.lucky(int(num[1]))
        return

    @staticmethod        
    def lucky(num):
        sum_left = 0
        sum_right = 0        
        for index,item in enumerate(str(num)):
            if index<3:
                sum_left  += int(item)
            else:
                sum_right += int(item)                
        if sum_left == sum_right:
            print('lucky')
        else:
            print('unlucky')          

# приложение-сервер принимает запросы вида: GET localhost:8081/lucky?num={number}}, 
# где number - это число на проверку счастливое ли число: сумма цифр справа равняется сумме чисел слева
# запрос можно послать например при помощи Postman
def main(): 
    print('starting listen port 8081...')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
main()