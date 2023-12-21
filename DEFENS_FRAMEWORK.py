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
import datetime as dt_module_custom
import threading as threading
import logging.handlers as handlers
from DDoS_Attack import DDoS_Attack
from ids_rule import ids_rules as ids_rules 
from deadman_switch import DeadmanSwitch
from Honeypot import Honeypot as Honeypot

class Honeypot:
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

    def DDoS_Attacker(self, attacker_ip, attacker_port):
        ddos_attack = DDoS_Attack(attacker_ip, attacker_port, self.honeypots[0].ip_address, self.honeypots[0].port, 5, 10)
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
