import socket

HOST = input("Digite o IP: ")
PORTS = range(1, 65536)

for port in PORTS:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((HOST, port))
            s.send(b'GET / HTTP/1.1\r\nHost: ' + HOST.encode() + b'\r\n\r\n')
            response = s.recv(1024)
            print(f'Porta {port}: {response.decode().strip()}')
        except (socket.timeout, ConnectionRefusedError):
            pass
        except Exception:
            pass
