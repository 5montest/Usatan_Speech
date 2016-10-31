# _*_ coding: utf-8 _*_
#!/usr/bin/env python

import subprocess
import time

p = subprocess.Popen(["bash Wait_mode.sh"], stdout=subprocess.PIPE, shell=True)
pid = p.stdout.read()

p.kill()
subprocess.call(["kill" + pid], shell=True)

