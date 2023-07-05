import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m)

p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()
'the the'

import re
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)