import socket
import struct
import time

def main():
    host = '127.0.0.1'
    port = 12345
    sock = socket.socket()

    with sock:
        sock.connect((host, port))

        # join player
        while True:
            print("join_player")
            msg = parse_message("join_player")
            sock.send(msg)
            print(msg)
            print(sock.recv(4096))
            time.sleep(1)

        while True:
            print(">>> ", end='')
            msg = input()

            if msg == "quit":
                break

            if is_test_command(msg):
                msg = parse_message(msg)
                sock.send(msg)
                continue

            if len(msg) == 0:
                continue

            sock.send(bytes(msg, 'utf-8'))

def is_test_command(msg):
    cmd_list = [
        "join_player"
    ]
    return msg in cmd_list


def parse_message(msg):
    if msg == "join_player":
        return struct.pack("<BH", 100, 1)

    return ''

if __name__ == '__main__':
    main()
