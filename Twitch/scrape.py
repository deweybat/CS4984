from emoji import demojize
import logging
import socket

logging.basicConfig(level = logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('singsing.log', encoding='utf-8')])
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'deweybat'
token = 'oauth:g257rwnua4djaax5yptxiqclji8g23'
channel = '#singsing'

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    elif len(resp) > 0:
        logging.infodemojize(resp))
