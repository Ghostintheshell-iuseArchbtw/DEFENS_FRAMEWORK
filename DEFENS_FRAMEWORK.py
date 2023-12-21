#######################################################################################################################
######################################## THE DEFENS Framework #########################################################
##########The DEFENS Framework is a framework that is used to defend against cyber attacks.############################
##########The DEFENS Framework takes it a step futher by retailating against your attacker(s)########################## 
##########As soon as an intrusion is detected. DEFENS will begin its defenese and ****ATTACK**** ****AUTOMATICALY****##
##########THIS TOOL IF USED INCORRECTLY CAN BE VERY DANGEROUS AND IS NOT RECOMMENDED FOR BEGINNERS#####################
##########ATTACKING SOMEONE WITHOUT THEIR PERMISSION IS ILLEGAL AND CAN GET YOU IN SERIOUS LEGAL TROUBLE###############
##########IT DOESNT MATTER IF THEY ATTACKED YOU FIRST##################################################################
##########THE DEFENS FRAMEWORK AND ITS CREATOR(s) ARE NOT RESPONSIBLE FOR ANY DAMAGES OR LEGAL TROUBLE THAT MAY OCCUR##
##########YOU HAVE BEEN WARNED,ONLY USE IN AN ETHICAL MANNER WITH REGARD TO YOUR LOCAL LAWS############################
#######################################################################################################################

import socket
import threading
import subprocess
from DDoS_Attack import DdosAttack
from deadman_switch import DeadmanSwitch
from honeypot import Honeypot
from ids_rule import IDSRule

class SocketWrapper:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.sendall(data.encode())

    def receive(self, buffer_size):
        return self.socket.recv(buffer_size).decode()

    def close(self):
        self.socket.close()

class DdosAttack(threading.Thread):
    def __init__(self, target_ip, target_port, attacker_ip, attacker_port, num_threads, num_requests):
        threading.Thread.__init__(self)
        self.target_ip = target_ip
        self.target_port = target_port
        self.attacker_ip = attacker_ip
        self.attacker_port = attacker_port
        self.num_threads = num_threads
        self.num_requests = num_requests

    def run(self):
        print("Performing DDoS attack...")
        subprocess.run(["python", "DDoS_Attack.py"])

class DeadmanSwitch(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Running the deadman switch...")
        subprocess.run(["python", "deadman_switch.py"])

class DefenseFramework:
    def __init__(self):
        self.honeypots = []
        self.ids_rules = []
    
    def build_honeypots(self):
        localhost = "127.0.0.1"
        honeypot1 = Honeypot(localhost, 4040)
        honeypot2 = Honeypot(localhost, 8080)
        self.honeypots = [honeypot1, honeypot2]

    def is_attacker_detected(self, attacker_ip):
        print("Checking if the attacker's IP address is detected...")
        for honeypot in self.honeypots:
            if honeypot.has_connection_from(attacker_ip):
                return True
        return False

    def build_ids(self):
        localhost = "127.0.0.1"
        ids_rule = IDSRule(localhost, "BLOCK")
        self.ids_rules.append(ids_rule)

    def ddos_attacker(self, attacker_ip, attacker_port):
        ddos_attack = DdosAttack(attacker_ip, attacker_port, self.honeypots[0].ip_address, self.honeypots[0].port, 5, 10)
        ddos_attack.run()

    def import_deadman_switch(self):
        if self.is_attacker_detected(self.honeypots[0].ip_address):
            deadman_switch = DeadmanSwitch()
            deadman_switch.run()

    def import_modules(self):
        print("Importing modules...")

    def run(self):
        self.build_honeypots()
        self.build_ids()
        self.import_modules()
        self.import_deadman_switch()

class Honeypot:      
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.logged_connections = []

    def log_connection(self, ip_address):
        self.logged_connections.append(ip_address)

    def has_connection_from(self, ip_address):
        return ip_address in self.logged_connections

class IDSRule:
    def __init__(self, ip_address, action):
        self.ip_address = ip_address
        self.action = action

# Create an instance of the DefenseFramework class and run the framework
defense_framework = DefenseFramework()
defense_framework.run()
