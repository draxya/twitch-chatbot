import socket
import re

# Connect to Twitch IRC
HOST = "irc.twitch.tv"
PORT = 6667
NICK = "your_bot_username"
PASS = "your_bot_oauth_token"
CHAN = "your_channel_name"

s = socket.socket()
s.connect((HOST, PORT))
s.send(f"PASS {PASS}\n".encode("utf-8"))
s.send(f"NICK {NICK}\n".encode("utf-8"))
s.send(f"JOIN #{CHAN}\n".encode("utf-8"))

# Define commands
commands = {
    "!hello": "Hello, World!",
    "!time": "The time is currently: " + time.strftime("%H:%M:%S"),
}

# Handle messages
while True:
    response = s.recv(2048).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)  # extract username
        message = CHAN + " :" + response.split(":")[2]  # extract message
        print(username + ": " + message)
        
        for command, reply in commands.items():
            if message.startswith(command):
                s.send(f"PRIVMSG #{CHAN} :{reply}\n".encode("utf-8"))
                break
