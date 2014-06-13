import subprocess

def get_config():
	output = subprocess.check_output(['zpool', 'status', '-v'])
	raw_pooldata = output.split('pool:')
	
	config_found = False
	for raw_pool in raw_pooldata
		for line in raw_pool.splitlines():
			line = line.strip()
			if line.startswith('pool:'):
				name = line.split('pool:',1)[1].strip()
				print "NAME: " + name
			if line.startswith('state:'):
				state = line.split('state:',1)[1].strip()
				print "STATE: " + state
			if line.startswith('scan:'):
				scan = line.split('scan:',1)[1].strip()
				print "SCAN: " + scan
			
			if line.startswith('errors:'):
				errors = line.split('errors:',1)[1].strip()
				print "ERRORS: " + errors
				
			if line.startswith('config:'):
				config_found = True
		
		if config_found:
			config = output.split('config:',1)[1]
			print "CONFIG: " + config
		
			