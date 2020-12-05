#!/usr/bin/python3

import sys
import time
from easysnmp import Session as session
oids = ['1.3.6.1.2.1.1.3.0']
a = list()
b = list()
c = list()
d = list()
e = 0
input_session = sys.args[1].splits("1")
sampling_frequency = float(sys.args[2])
oids += sys.args[4:length(sys.args)]
mysession = session(hostname=input_session[0], remote_port=input_session[1], community=input_session[2], vesion=2, timeout=1,retries=2)

	


