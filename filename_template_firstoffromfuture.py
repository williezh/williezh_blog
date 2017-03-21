#/usr/bin/env python
#coding=utf-8
import os
import re
fn="venv/lib/site-packages/zinnia_bootstrap/templates/comments/zinnia/entry/form.html"
fullpath=os.path.join(os.getcwd(),'{}'.format(fn))
print(fullpath)
tobedel=r"\{% load 'firstof' from future %\}"
with open(fullpath) as f:
	s=f.read()
if re.search(tobedel,s):
	with open(fullpath,'w') as wf:
		wf.write(re.sub(tobedel,'',s))

