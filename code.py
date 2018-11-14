import sys

def help():
	if len(sys.argv) < 3:
		print("Uso: pyhton "+sys.argv[0]+" <arq_mem_prin> <arq_mem_cache>")

if __name__ == '__main__':
#dram 32 posicoes
#cash 8 posicoes
	
	#help()
	dram = []
	cache = ['0' for i in range(8)]
	buffer_entrada = []
	print(dram)
	#"""
	with open(sys.argv[1], 'r') as f:
		for i in range(32):
			dram.append(f.readline().replace('\n',''))
	
	with open(sys.argv[2], 'r') as f:
		while True:
			line = f.readline().replace('\n','')
			if line == "":
				break

			buffer_entrada.append(line)


	print(dram)
	print(buffer_entrada)
