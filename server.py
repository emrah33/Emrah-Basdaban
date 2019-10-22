import socket

s = socket.socket()
host = socket.gethostname()
port = 27018
s.bind((host,port))
s.listen(3)
print(host)
print("Port Dinleme Moduna Geçti.")
conn, addr = s.accept()
print(addr, "Diğer Bilgisayar Bağlandı.")

filename = input(str("Göndereceğiniz dosyanın adını yazınız uzantısıyla birlikte. (deneme.txt) : "))
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Dosya Diğer Bilgisayara Gönderildi")
