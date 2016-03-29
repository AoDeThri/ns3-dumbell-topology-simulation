import os
import subprocess
import re

files = [f for f in os.listdir('.') if re.match(r'^application', f)]

for f1 in files:
	if not re.search(r'congestion', f1):
		proc = subprocess.Popen(['gnuplot','-p'], 
				        shell=True,
				        stdin=subprocess.PIPE,
				        )
		proc.stdin.write('set terminal png size 1200,1000\n')
		proc.stdin.write('set output "'+f1+'.png"\n')
		proc.stdin.write("plot '"+f1+"' using 1:2 title '"+f1+"' with linespoints\n")
		proc.stdin.write("exit")

