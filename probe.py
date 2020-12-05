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
oids += sys.argv[4:len(sys.argv)]
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

    for j in range(1,len(a)):
        b.append(int(a[j].value))

        t2.append(t)
        if (i>0 and len(x)>0):
           if b[j-1]-x[j-1]<0:
              e=a[j].snmp_type
              if e=='COUNTER':
                 b[j-1]=b[j-1]+2**32
              elif e=='COUNTER64':
                   b[j-1]=b[j-1]+2**64
           else:
             #print(Nr)
              Nr=b[j-1]-x[j-1]
              td=round((t2[j-1]-y[j-1]),1)
              dr.append(int(Nr/td))
             #print(dr)

           if len(dr)==len(a)-1:
            den=str(dr)[1:-1]
            den = den.replace(",", "|")
            print(int(t),"|",den)
    tf=time.time()
    time.sleep((1/sampling_frequency)-(tf-t))
    x=b
    y=t2
    z=dr