import random
import sys

# Essa lista irá armazenar qual o número de vezes que uma
# determinada posição da memória cache foi acessada.
contador_lfu = {}



class Memoria:
    def __init__(self, tamanho_cache, qtd_conjuntos):
        self.cache = {} # memória cache
        self.hits = 0 # numero de hits
        self.miss = 0 # numero de misses
        self.tamanho_cache = tamanho_cache # tamanho da cache
        self.qtd_conjuntos = qtd_conjuntos # quantidade total de conjuntos


    def init_cache(self):
        """ Cria uma memória cache zerada utilizando dicionários (chave, valor) e com
            valor padrão igual a '-1'
            popula a memória cache com o valor -1, isso indica que a posição não foi usada
        """
        for x in range(0, self.tamanho_cache):
            self.cache[x] = -1

    def init_lfu(self):
        """
          Seta os valores do contador LFU para zero, ou seja, a posição de memória que ocupa aquela
          posição da cache ainda não foi utilizada. Para cada posição da cache teremos um contador
          que será somado tada vez que houver um CACHE HIT e, será zerado quando a posição for substituida
        """
        # cria on contador LFU uma posiçõao para caqda posição de memória
        for x in range(0, self.tamanho_cache):
            contador_lfu[x] = 0

    def hit(self, posicao_memoria):
        """
            Verifica se uma determinada posição de memória está na cache


        :param posicao_memoria:
            posicao de memoria a ser testada
        :return:
            se deu hit ou nao, se deu hit retorna a posicao
        """

        # a divisao de conjuntos, olhando em q posicao ela estaria
        num_conjunto = int(posicao_memoria) % int(self.qtd_conjuntos)

        while num_conjunto < self.tamanho_cache:
            if self.cache[num_conjunto] == posicao_memoria:
                return num_conjunto

            # pula o tamanho do conjunto
            num_conjunto += self.qtd_conjuntos

        # não achou a posição de memória na cache
        return -1

    def get_cache_conjunto(self, num_conjunto):
        """
        Retorna uma lista com todas as posições da memória cache que fazem
            parte de um determinado conjunto.

        :param num_conjunto:
            {int} -- número do conjunto que se quer saber quais são os endereçamentos associados com aquele conjunto
        :return:
            [list] -- lista de posições de memória associada com um conjunto em particular
        """

        lista_posicoes = []
        posicao_inicial = num_conjunto
        while posicao_inicial < self.tamanho_cache:
            lista_posicoes.append(posicao_inicial)
            posicao_inicial += self.qtd_conjuntos

        return lista_posicoes

    def LFU(self, posicao_memoria):
        """
            Nessa politica de substituição, o elemento que é menos acessado é removido da
            memória cache quando ocorrer um CACHE MISS. A cada CACHE HIT a posição do HIT ganha um ponto
            de acesso, isso é usado como contador para saber qual posição deve ser removida no caso de CACHE MISS.

        :param posicao_memoria: posicao de memoria q sera acessada
        :return:
        """
        num_conjunto = int(posicao_memoria) % int(self.qtd_conjuntos)
        list_posicoes = self.get_cache_conjunto(num_conjunto)

        # descobrir dentro do conjunto qual posição da cache tem menos acessos
        posicao_substituir = 0
        if len(list_posicoes) > 1:

            # descobrir qual das posições é menos usada
            list_qtd_acessos = []
            for qtd_acessos in list_posicoes:
                list_qtd_acessos.append(contador_lfu[qtd_acessos])

            posicoes_com_menos_acesso = min(list_qtd_acessos)
            candidatos_lfu = []

            for qtd_acessos in list_posicoes:
                if contador_lfu[qtd_acessos] == posicoes_com_menos_acesso:
                    candidatos_lfu.append(qtd_acessos)

            # para garantir ordem aleatória de escolha caso duas ou mais posições
            # tenham o mesmo número de acessos
            posicao_substituir = random.choice(candidatos_lfu)

        # zera o número de acessos a posição que foi substituida
        contador_lfu[posicao_substituir] = 0

        # altera a posição de memória que está na cache
        self.cache[posicao_substituir] = posicao_memoria

    def exec(self, mem_acess):
        """
            executa a operacao de mapeamento associativo por conjuntos
        :param qtd_conjuntos: numero de conjuntos na cache
        :param mem_acess: lista com posicoes de memorias acessada
        :return:

        """
        self.init_cache()
        self.init_lfu()

        # percorre cada uma das posições de memória que estavam no arquivo
        for index, posicao_memoria in enumerate(mem_acess):
            print('\n\n\nIteração número: {}'.format(index + 1))
            # verificar se existe ou não a posição de memória desejada na cache
            posit_cache = self.hit(posicao_memoria)

            # a posição desejada já está na memória
            if posit_cache >= 0:
                #### HIT ####
                self.hits += 1
                print('Cache HIT: posiçao de memória {}, posição cache {}'.format(posicao_memoria, posit_cache))
                contador_lfu[posit_cache] += 1

            else:
                #### MISS ####
                self.miss += 1
                print('Cache MISS: posiçao de memória {}'.format(posicao_memoria))

                # verifica se existe uma posição vazia na cache NAQUELE CONJUNTO, se sim aloca nela a posição de memória
                posicao_vazia = self.posicao_vazia(posicao_memoria)

                if posicao_vazia>=0:
                    self.cache[posicao_vazia] = posicao_memoria
                else:
                    # se n tem posicao vazia
                    self.LFU(posicao_memoria)

        print('\n\n-----------------')
        print('Resumo Mapeamento 4-way-associative')
        print('-----------------')
        print('Política de Substituição: LFU')
        print('-----------------')
        print('Total de memórias acessadas: {}'.format(len(mem_acess)))
        print('Total HIT {}'.format(self.hits))
        print('Total MISS {}'.format(self.miss))
        taxa_cache_hit = (self.hits/ len(mem_acess)) * 100
        print('Taxa de Cache HIT {number:.{digits}f}%'.format(number=taxa_cache_hit, digits=2))

    def posicao_vazia(self, posicao_memoria):
        """
            Verifica se existe na cache uma posição de memória que ainda não foi utilizada,
            se existir, essa posição é retornada.

        :param posicao_memoria: posicao da memoria q se quer armazenar na cache
        :return: primeira posicao de memoria vazia do CONJUNTO
        """
        num_conjunto = int(posicao_memoria) % int(self.qtd_conjuntos)
        list_posicoes = self.get_cache_conjunto(num_conjunto)

        # verifica se alguma das posições daquele conjunto está vazia
        for x in list_posicoes:
            if self.cache[x] == -1:
                return x
        return -1

def help():
    if len(sys.argv) < 3:
        print("Uso: python3 "+sys.argv[0]+" <arg-lista_busca> <arq-mem_prin>")
        sys.exit()

if __name__ == '__main__':
	
    	
    procura_cache = [] #lista com as posicoes para serem buscadas na memoria principal
    dram = {}
    
    help()

    #leitura do arquivo de busca na cache
    with open(sys.argv[1],'r') as f:
        while True:
            line = f.readline().replace('\n','')
            if line == "":
                break
            procura_cache.append(line)

    #leitrura do arquivo para carregar a memoria principal
    with open (sys.argv[2], 'r') as f:
        for i in range(32):
            dram['{0:05b}'.format(i)] = f.readline().replace('\n','')

    print(procura_cache)
    print('\n\n',dram)

    cache = Memoria(8,4)
    cache.exec(procura_cache)
