import socket
from _thread import *

server = "192.168.0.106"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("\nServer Started!!! Waiting for client connection....")

def read_pos(data):
    try:
        x, y = map(int, data.split(","))
        return x, y
    except:
        return 0, 0

def make_pos(tup):
    return f"{tup[0]},{tup[1]}"

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    try:
        conn.send(str.encode(make_pos(pos[player])))
    except Exception as e:
        print(f"Error sending initial position: {e}")
        return

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                print("Disconnected")
                break

            data = read_pos(data)
            pos[player] = data
            reply = pos[1 - player]
            print("Received:", data)
            print("Sending:", reply)
            conn.sendall(str.encode(make_pos(reply)))

        except Exception as e:
            print(f"Error: {e}")
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
