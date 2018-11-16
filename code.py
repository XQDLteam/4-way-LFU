import sys

def help():
	if len(sys.argv) < 3:
		print("Uso: pyhton "+sys.argv[0]+" <arq_mem_prin> <arq_mem_cache>")
		sys.exit()
if __name__ == '__main__':
#dram 32 posicoes
#cash 8 posicoes
#
	help()
	dram = {}
	cache = {'{0:05b}'.format(i) for i in range(8)}
	cache = dict.fromkeys(cache, '0')
	buffer_entrada = []
	
	with open(sys.argv[1], 'r') as f:
		for i in range(32):
			dram['{0:05b}'.format(i)] = f.readline().replace('\n','')
	
	with open(sys.argv[2], 'r') as f:
		while True:
			line = f.readline().replace('\n','')
			if line == "":
				break

			buffer_entrada.append(line)
	
	#print(dram,'\n\n',sorted(dram.items(), key=lambda x : x[0]))
	#print('\n', buffer_entrada)
	#print('\n', sorted(cache.items(), key=lambda x : x[0]))
