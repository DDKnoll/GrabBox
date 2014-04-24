# First make sure we have Sudo permissions and NPM.
# If not, then print an error message.
# 
# Then install requirements using NPM

import subprocess

args = ['which','npm']

npm = subprocess.check_output('which npm', shell=True)
if( npm.find('npm') == -1 ):
	print "You must install npm before running this application."	
	quit()
