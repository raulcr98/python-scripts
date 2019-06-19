import os

def do_ping(ip):
    print ("HACIENDO PING A " + str(ip))
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True
    else:
        return False

ip = input("Introduce la ip: ")

while True:
    ok = do_ping(ip)
    if ok:
        cont = 500
        while cont > 0:
            os.system("echo -ne '\a'")
            cont -= 1
        os.system("clear")
        print ('''
                ##############################################
                ######             IP ONLINE              ####
                ##############################################
            ''')
        break
