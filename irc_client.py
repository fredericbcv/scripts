import os, sys, socket, time, string, argparse, select
from threading import Thread

class irc_client(object):
    def __init__(self, *args, **kwarg):
        self.host = args[0]
        self.nickname = args[1]
        self.port = kwarg.get('port',6667)
        self.console = kwarg.get('console',True)
    
        # Open IRC host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
            print("[+] Connecting to " + self.host + ":" + str(self.port))
        except socket.error:
            print("[-] Connection failed")
            sys.exit()

        # Set Nick & User name
        user = self.nickname + " 0 * :" + self.nickname
        self.socket.send(str("NICK "+self.nickname+"\r\n").encode())
        self.socket.send(str("USER "+user+"\r\n").encode())

        # Wait for non console mode
        time.sleep(1)

        if self.console:
            # Open IRC Reader
            th_reader = Thread(target=self.reader)
            th_reader.daemon = True
            th_reader.start()

            kill = False
            while not kill:
                try:
                    time.sleep(1)
                    tmp_input = input('')
                    self.socket.send(str(tmp_input+"\r\n").encode())
                except KeyboardInterrupt:
                    print("[+] Exiting")
                    kill = True
            # Close socket
            self.socket.close()

    def send(self,msg):
        self.socket.send(str(msg+"\r\n").encode())

    def read(self):
        time.sleep(0.1)
        return self.socket.recv(4096).decode()

    def reader(self):
        while True:
            msg_list = self.socket.recv(4096).decode().split('\r\n')
            msg_list = filter(lambda x: x != '',msg_list)
            for msg in msg_list:
                if "PING" in msg:
                    self.socket.send(str('PONG '+msg[4:]+'\r\n').encode())
                else:
                    print (msg)

def get_args():
    parser = argparse.ArgumentParser(
        description="Simple IRC client"
    )
    parser.add_argument('host')
    parser.add_argument('nickname')
    parser.add_argument('-p', '--port', default=6667, type=int)
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    irc_client(args.host,args.nickname,port=args.port,console=True)