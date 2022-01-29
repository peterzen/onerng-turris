#!/usr/bin/python
#
#	OneRNG firmware verification
#	(C) Copyright Paul Campbell Moonbase Otago 2014
#
import sys
import tempfile
import gnupg
import syslog

def failure(why):
	syslog.syslog(syslog.LOG_ERR, "firmware verification failed: "+why)
	sys.exit(1)

syslog.openlog("OneRNG");
state = 0
public_key = """\
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

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
=IjnI
-----END PGP PUBLIC KEY BLOCK-----
"""

state=0
length = 0
version = 0
with open(sys.argv[1], 'rb') as f:
	while True:
		c = f.read(1)
		if len(c) == 0:
			failure("Short image")
		if sys.version_info[0] >= 3:
			x = c[0]
		else:
			x = ord(c[0])
		if state == 0:
			if x == 0xfe:
				state = 1
		elif state == 1:
			if x == 0xed:
				state = 2
			else:
				state = 0
		elif state == 2:
			if x == 0xbe:
				state = 3
			else:
				state = 0
		elif state == 3:
			if x == 0xef:
				state = 4
			else:
				state = 0
		elif state == 4:
			if x == 0x20:
				state = 5
			else:
				state = 0
		elif state == 5:
			if x == 0x14:
				state = 6
			else:
				state = 0
		elif state == 6:
			length = x
			state = 7
		elif state == 7:
			length = length|(x<<8)
			state = 8
		elif state == 8:
			length = length|(x<<16)
			state = 9
		elif state == 9:
			version = x
			state = 10
		elif state == 10:
			version = version|(x<<8)
			state = 11
		elif state == 11:
			state = 12
		elif state == 12:
			c = f.read(length)
			f.close
			if len(c) != length: 
				failure("Bad image")
			if version >= 3:
				end_off = 680
			else:
				end_off = 600
			if sys.version_info[0] >= 3:
				x = c[length-end_off+0]
				klen = x;
				x = c[length-end_off+1]
			else:
				x = ord(c[length-end_off+0])
				klen = x;
				x = ord(c[length-end_off+1])
			klen = klen|(x<<8)
			sig = tempfile.NamedTemporaryFile()
			sig.write(c[length-end_off+2:length-end_off+2+klen])    # signature
			gpg = gnupg.GPG()
			gpg.import_keys(public_key)
			sig.flush()
			verified = gpg.verify_data(sig.name, c[0:length-end_off])
			sig.close()
			if verified:
				syslog.syslog(syslog.LOG_NOTICE, "firmware verification passed OK - version="+str(version))
				sys.exit(0)
			failure("Invalid firmware signature")
		else:
			state = 0
	f.close();
failure("System problem")

