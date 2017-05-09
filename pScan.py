#!/usr/bin/python
import sys, argparse, socket

def main():
	try:
		p = argparse.ArgumentParser(description='Port scanner')
		req = p.add_argument_group('required arguments')
		req.add_argument('-t', '--target', dest='target', help='Target IP address or hostname')
		req.add_argument('-s', '--start', dest='start', help='Starting port')
		req.add_argument('-e', '--end', dest='end', help='Ending port')
		args = p.parse_args()
		# parses arguments

		target = args.target
		start = int(args.start)
		end = int(args.end)

		if 'http://' in target:
			target = target.replace('http://', '')

		elif 'https://' in target:
			target = target.replace('https://', '')

		else:
			pass

		ip = socket.gethostbyaddr(target)
		target = str(ip[2]).replace('[', '').replace(']', '').replace('\'', '')
		# checks to see if URL is valid

		print 'Scanning... '

		for port in range(start, end + 1):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((target, port))
			# checks to see if port is open

			if result == 0:
				print 'Port %s:     Open' % (port)

			else:
				pass

		sys

	except socket.gaierror:
		print 'Invalid URL'
		sys.exit()

	except TypeError:
		print './pScan.py -h for help'
		sys.exit()

	except KeyboardInterrupt:
		sys.exit()

main()
