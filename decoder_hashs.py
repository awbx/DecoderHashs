#######################################################################
#				Decoder Hashs Version 1.0 By AwBxKing				  #
#					Contact Us :Fb->awbx.king.9						  #					
#######################################################################
import hashlib
import logo
import time,os,sys
import argparse


def decode(**kwargs):
	algorithm	= kwargs['algorithm']
	hashvalue 	= kwargs['hashvalue']
	wordlist 	= kwargs['wordlist']
	try:
		os.system('clear && clear')
		logo.logo()
		print(logo.bcolors.HEADER,'please Wiat...!')
		with open(wordlist,'r+') as file :
			reads 		= file.readlines()
			start = time.strftime('%s')
			for i in reads:
				i 		= i.strip('\n')
				h 		= hashlib.new(algorithm)
				value 	= bytes(i,encoding='utf8')
				h.update(value)
				res 	= h.hexdigest()
				if res == hashvalue :
					print('Password Cracked :[%s : %s]' % (hashvalue,i))
					end = time.strftime('%s')
					totaltime = int(end) - int(start)
					print('Password Cracked in %s Second' % totaltime)
					return True
					break;
	except KeyboardInterrupt :
		print('\rGood Bye ^_^')
		sys.exit()
	except FileNotFoundError as e:
		print('Wordlist Not Found : %s '% e)
	except ValueError as e:
		print('Algorithm Unknown : %s'%e)
	except :
		print('Error ')
		sys.exit()
opt = argparse.ArgumentParser(description="Docoder Hashs By AwBxKing")
opt.add_argument('-a','--algorithm',dest='algorithm',help='Enter Algorithm Of Encryption Type')
opt.add_argument('-H' ,'--hashvalue',dest='hashvalue',help='Enter Your Hash To Decode')
opt.add_argument('-w' ,'--wordlist',dest='wordlist',help='Enter File Wordlist Passwords')
opt.add_argument('-v','--version',dest='version',help='Put OK To Print Version & exit',default='')
option = opt.parse_args()

if option.version.lower() =='ok' :
	print('Decoder Hash Version 1.0 By AwBxKing -_-')
elif option.algorithm != None and option.wordlist !=None and option.hashvalue !=None :
	result = decode(algorithm=option.algorithm,hashvalue=option.hashvalue,wordlist=option.wordlist)
	if result !=True :
		print('Password Not Cracrked ! Try Another Wordlist')
elif len(sys.argv) == 1 :
	opt.print_help()
	sys.exit()
else :
	sys.exit()