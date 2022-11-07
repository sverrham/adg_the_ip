import argparse
import os
import socket
import sys
from _thread import start_new_thread

from Processor import Processor
from ordersystem import OrderSystem
from story import Story

paser = argparse.ArgumentParser(prog="adg_server",
                                description = "meaningless port server programs")
paser.add_argument('-p', '--port', type=int, default=12345)

args = paser.parse_args()

portprogram = {12389: 0, 12287: 1, 12346: 2, 12347: 3, 14431: 4}
programs = [{"h":"There is no help for you!", "help":"There is no help for you!"},
            {"adg":"The code you should send in is qASbb1234!"},
            {"sverre":"The code you should send in is bananas1234"},
            {"team":"The code you should send in is Unberibable!"},
            {"h": "questions, answers and more", "help": "questions, answers and more",
             "questions":"ports has strange access strings.",
             "answers":"user and login info can be obtained on the image.",
             "more":"have you tried steganography in the image?"}]

storya = [{"story": "a room full of people\r\n", "search": "interesting there are more rooms, we blindly wander to the next.\r\n"},
           {"story": "there is a view, just like me but you can't see, can we go somewhere\r\n", "left": "We walk and we walk, did you know there are ports with codes hidden?\r\n"},
           {"story": "the talking of people diminishes as we walk, strange that this suddenly is a cave...\r\n", "look": "that was not smart, looking up and walking we miss the black hole in the floor...\r\n and doooooooooooown we goooooo!\r\n"},
           {"story": "some ports respond to my name, some to what we are, and some to what we now do...\r\n", "search": "smarter to search this place, patting down slow, slow, remembering the light on the phone in your pocket, with it on we can see.\r\n only cold hard walls all around.\r\n"},
           {"story": "Where the 12345 am I\r\n", "kick": "You kick the wall with tremendous fource like bruce lee!\r\n"},
           {"story": "what the hell is going on, you think as the kick resonates in the room\r\na click is heard from the corner and a hatch opens up, how far can this go?", "down": "down the hatch we gooooo.\r\n"}]

HOST = ''  # all available interfaces
PORT = args.port # arbitrary non privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error as msg:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############


def client_thread(conn, ip_addr):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    f = open("logs/{}-{}.log".format(PORT, ip_addr), "a")

    processor = None
    if PORT == 12345:
        processor = OrderSystem()
    elif PORT == 11111:
        processor = Story(storya)
    else:
        processor = Processor(programs[portprogram[PORT]])

    while True:
        data = conn.recv(1024)
        if not data:
            continue

        try:
            ret = processor.process(data.decode("utf-8"))
            f.write(data.decode("utf-8"))
            f.flush()
        except Exception as e:
            print(e)
            ret = None

        if ret is None:
            break
        conn.send(ret.encode("utf-8"))

    f.close()
    conn.close()


while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn, addr[0],))

s.close()
