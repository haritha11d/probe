#!/usr/bin/python3

import sys
import time
from easysnmp import Session as session
oids = ['1.3.6.1.2.1.1.3.0']
x = list()
b = list()
dr = list()
Nr = list()
tf = 0
input_session = sys.argv[1].splits("1")
sampling_frequency = float(sys.argv[2])
oids += sys.argv[4:length(sys.argv)]
mysession = session(hostname=input_session[0], remote_port=input_session[1], community=input_session[2], vesion=2, timeout=1,retries=2)


for i in range(Nosamples+1):
    t=time.time()
    a=mysession.get(oids)
    b=[]
    t2=[]
    dr=[]

    for f in range(len(oids)):
        if a[f].value=='NOSUCHINSTANCE':
           del(a[f])