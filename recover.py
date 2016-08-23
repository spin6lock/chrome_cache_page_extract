import re
from binascii import unhexlify
from gzip import GzipFile
from itertools import chain
from StringIO import StringIO
 
with open("cache.html", "rb") as f:
    html = f.read().decode("utf-8")
    hexlines = re.findall("<pre>(.*?)</pre>", html, flags=re.S)[2].splitlines()
    hexdata = ''.join(chain.from_iterable(l[10:58].split() for l in hexlines))
    print GzipFile(fileobj=StringIO(unhexlify(hexdata))).read()
