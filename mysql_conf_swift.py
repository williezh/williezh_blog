#coding=utf-8
import sys
import re
fn='williezh_blog/local_settings.py'
with open(fn) as f:
    s=f.read()
n="'slave'"
n2="'default'"
if len(sys.argv)>1:
    n,n2=n2,n
if re.search(n,s):
    with open(fn,'w') as wf:
        wf.write(re.sub(n,n2,s))
