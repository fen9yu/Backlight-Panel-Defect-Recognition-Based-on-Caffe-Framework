import re

flag=0
with open('testresult', 'r') as f:
    for line in f.readlines():
        m=re.match(r'^predicted label: (\d)',line)
        if int(m.group(1))==1:
            print('The image has defect(s).')
            flag=1
            break
if flag==0:
    print('The image is good.')