import matplotlib.pyplot as plt


# Função para apresentar o menu
def menu():
    print('\n 0 - Sair\n 1 - Cadastrar Paciente\n 2 - Listar Pacientes\n 3 - Atualizar Status\n 4 - Listar por Status\n'
          ' 5 - Bairros mais Infectados\n 6 - Taxa de Crescimento\n 7 - Quantidade de Infectados por Genero\n'
          ' 8 - Exibir Infectados por Idade\n 9 - Porcentagem de Curados\n10 - Exibir Grafico')


# Função que contém os quatro status do paciente
def statusPacientes():
    statu = ('CURADO', 'ISOLAMENTO DOMICILIAR', 'INTERNADO', 'OBITO')
    return statu


# Função que contém os possiveis resultados do exame
def testeOpcoes():
    teste = ('NEGATIVO', 'POSITIVO-SWAB', 'POSITIVO-IGMIGG', 'POSITIVO-IGG')
    return teste


# Função para gerar os dias e as semanas
def gerarSemanas():
    semana = {1: list(), 2: list(), 3: list(), 4: list()}
    for i in range(1, 32):
        if i >= 1 and i <= 7:
            semana.get(1).append(i)
        elif i >= 8 and i <= 14:
            semana.get(2).append(i)
        elif i >= 15 and i <= 21:
            semana.get(3).append(i)
        else:
            semana.get(4).append(i)
    return semana


# Requisito 1:
def cadastraPessoa(paci, tes):
    '''
    paci recebe o dicionário de pacientes
    tes recebe a função "testeOpcoes"
    '''
    # Adicionar ID para o paciente
    t = len(paci) + 1
    nome = str(input('Digite um nome: ')).upper().strip()
    # verificar dados que o usuário insere
    while nome == '' or nome.isspace():
        nome = str(input('Nome invalido. Digite novamente: '))
    idade = int(input('Insira uma idade: '))
    while idade <= 0 or idade >= 120:
        idade = int(input('Idade inválida tente novamente: '))
    bairro = str(input('Digite um bairro: ')).upper().strip()
    while bairro == '' or bairro.isspace():
        bairro = str(input('Bairro invalido. Digite novamente '))
    genero = input('Digite um genero "F" ou "M": ').upper().strip()
    while genero not in 'F' and genero not in 'M' or genero == '' or genero.isspace():
        genero = input('Genero inválido tente novamente: F/M: ').upper().strip()
    dia = int(input('Digite um dia: '))
    while dia < 1 or dia > 31:
        dia = int(input('dia inválido,digite um dia válido: '))
    mes = int(input('Em qual mês foi infectado? '))
    while mes < 1 or mes > 12:
        mes = int(input('Mês inválido, digite um mês válido: '))
    resultadoTeste = int(input(
        'Qual o resultado do paciente?\n1 - Negativo;\n2 - Positivo-Swab\n3 - Positivo-IgmIgg\n4 - Positivo-Igg\n'))
    while resultadoTeste != 1 and resultadoTeste != 2 and resultadoTeste != 3 and resultadoTeste != 4:
        resultadoTeste = int(input(
            'Valor invalido. Tente novamente:\n1 - Negativo;\n2 - Positivo-Swab\n3 - Positivo-IgmIgg\n'
            '4 - Positivo-Igg\n'))
    if resultadoTeste == 2 or resultadoTeste == 3 or resultadoTeste == 4:
        paci[t] = [nome, idade, bairro, genero, dia, mes, tes[resultadoTeste - 1], 'ISOLAMENTO DOMICILIAR']
    print('Cadastro feito com sucesso.')


# Requisito 2:
def listar(paci):
    # Lista para apresentar as informações dos pacientes
    dadosColunas = ['ID', 'NOME', 'IDADE', 'BAIRRO', 'GENERO', 'DIA', 'MES', 'RESULTADO', 'STATUS']
    if len(paci) > 0:
        for i in dadosColunas:
            print('{:^26}'.format(i), end='')
        print()
        for k in paci:
            print('=' * 235)
            if paci.get(k)[7] == 'CURADO':
                # Colorindo os pacientes de status diferentes com as respectivas cores
                print('\x1b[5;30;46m{:^26}\x1b[0m'.format(k), end='')
                for v in paci.get(k):
                    print('\x1b[5;30;46m{:^26}\x1b[0m'.format(v), end='')
                print()
                print('=' * 235)
            elif paci.get(k)[7] == 'ISOLAMENTO DOMICILIAR':
                print('\x1b[5;30;47m{:^26}\x1b[0m'.format(k), end='')
                for v in paci.get(k):
                    print('\x1b[5;30;47m{:^26}\x1b[0m'.format(v), end='')
                print()
                print('=' * 235)
            elif paci.get(k)[7] == 'INTERNADO':
                print('\x1b[6;30;42m{:^26}\x1b[0m'.format(k), end='')
                for v in paci.get(k):
                    print('\x1b[6;30;42m{:^26}\x1b[0m'.format(v), end='')
                print()
                print('=' * 235)
            else:
                print('\x1b[5;30;41m{:^26}\x1b[0m'.format(k), end='')
                for v in paci.get(k):
                    print('\x1b[5;30;41m{:^26}\x1b[0m'.format(v), end='')
                print()
                print('=' * 235)
    else:
        print('Lista de pacientes vazia')


# Requisito 3:
def inserirStatus(paci, statu):
    '''
    statu recebe a função "statusPaciente"
    '''
    # Verificar se há pacientes no dicionário
    if len(paci) == 0:
        print('Nao ha pacientes cadastrados no sistema')
    else:
        # Variável usada para confirmar a decisão do usuário
        cont = 's'
        while cont == 's':
            # Variável para procurar pelos ID's
            busca = int(input('\nInsira um ID ou digite 0 para sair: '))
            if busca == 0:
                break
            for k in paci:
                if busca == k:
                    print(k, paci[k])
                    conf = str(input('\nEsse é o paciente que voce estava procurando? S/N ')).lower().strip()
                    while conf != 's' and conf != 'n':
                        conf = input('\nValor invalido. Digite "S" ou "N" ').lower().strip()
                    if conf == 's':
                        status = int(input('Digite uma das opçoes de status do paciente:\n1 - Curado\n'
                                           '2 - Isolamento Domiciliar\n3 - Internado\n4 - Obito\n'))
                        while status != 1 and status != 2 and status != 3 and status != 4:
                            status = int(input('\nValor invalido. Insira um status valido:\n1 - Curado\n'
                                               '2 - Isolamento Domiciliar\n3 - Internado\n4 - Obito\n'))
                        if status == 1:
                            del (paci.get(k)[7])
                            paci[k].append(statu[status - 1])
                        elif status == 2:
                            del (paci.get(k)[7])
                            paci[k].append(statu[status - 1])
                        elif status == 3:
                            del (paci.get(k)[7])
                            paci[k].append(statu[status - 1])
                        else:
                            del (paci.get(k)[7])
                            paci[k].append(statu[status - 1])
                        print('Status adicionados com sucesso')
                        cont = input('Deseja continuar a cadastrar status? S/N ').lower().strip()
                        while cont != 'n' and cont != 's':
                            cont = input('Valor invalido. Digite "S" ou "N" para continuar: ').lower().strip()
            if busca not in paci:
                print('ID nao cadastrado')


# Requisito 4:
def listarPorStatus(paci, statu):
    if len(paci) > 0:
        # Conjunto que armazena os status
        armStatus = set()
        dadosColunas = ['ID', 'NOME', 'IDADE', 'BAIRRO', 'GENERO', 'DIA', 'MES', 'RESULTADO', 'STATUS']
        # Variável para o usuário inserir o status
        statusProcurado = int(input('\nInsira um dos status para listar os pacientes\n1 - Curado\n'
                                    '2 - Isolamento Domiciliar\n3 - Internado\n4 - Obito\n'))
        while statusProcurado != 1 and statusProcurado != 2 and statusProcurado != 3 and statusProcurado != 4:
            statusProcurado = int(input('\nStatus invalido. Digite novamente um dos status\n1 - Curado\n'
                                        '2 - Isolamento Domiciliar\n3 - Internado\n4 - Obito\n'))
        for k in paci:
            armStatus.add(paci.get(k)[7])
            # Se a variável "armStatus" posuir todos os status possíveis o laço de repetição é quebrado
            if len(armStatus) == 4:
                break
        if statu[statusProcurado - 1] in armStatus:
            for j in dadosColunas:
                print('{:^26}'.format(j), end='')
            print()
            print('=' * 235)
            for i in paci:
                if statu[statusProcurado - 1] == paci.get(i)[7]:
                    # Coloridos os pacientes de status diferentes com as respectivas cores
                    if paci.get(i)[7] == 'CURADO':
                        print('\x1b[5;30;46m{:^26}\x1b[0m'.format(i), end='')
                        for v in paci.get(i):
                            print('\x1b[5;30;46m{:^26}\x1b[0m'.format(v), end='')
                        print()
                        print('=' * 235)
                    elif paci.get(i)[7] == 'ISOLAMENTO DOMICILIAR':
                        print('\x1b[5;30;47m{:^26}\x1b[0m'.format(i), end='')
                        for v in paci.get(i):
                            print('\x1b[5;30;47m{:^26}\x1b[0m'.format(v), end='')
                        print()
                        print('=' * 235)
                    elif paci.get(i)[7] == 'INTERNADO':
                        print('\x1b[6;30;42m{:^26}\x1b[0m'.format(i), end='')
                        for v in paci.get(i):
                            print('\x1b[6;30;42m{:^26}\x1b[0m'.format(v), end='')
                        print()
                        print('=' * 235)
                    else:
                        print('\x1b[5;30;41m{:^26}\x1b[0m'.format(i), end='')
                        for v in paci.get(i):
                            print('\x1b[5;30;41m{:^26}\x1b[0m'.format(v), end='')
                        print()
                        print('=' * 235)
        else:
            print('\nO status que procura nao existe na lista de pacientes')
    else:
        print('\nLista de pacientes vazia')


# Requisito 5:
def calcularBairro(paci):
    # Cotador de pessoas doentes
    n = 0
    # Listas para armazenar bairros infectadas
    bairrosInf = []
    # Lista que armazena o número de infectados
    numInf = []
    # Lista para armazenar as porcentagens
    porcenInf = []
    for k in paci:
        busca = paci.get(k)[2]
        if busca not in bairrosInf:
            bairrosInf.append(busca)
            for j in range(1, len(paci) + 1):
                if busca == paci[j][2]:
                    n += 1
            porcen = (n / len(paci)) * 100
            porcenInf.append(porcen)
            numInf.append(n)
        n = 0
    copiaNumInf = numInf.copy()
    copiaNumInf.sort(reverse=True)
    copiaNumInf2 = numInf
    copiaBairrosInf = bairrosInf.copy()
    print('{:<20} {:^20} {:>20}'.format('BAIRRO', 'QUANTIDADE', 'PORCENTAGEM'))
    for inf in copiaNumInf:
        ind = copiaNumInf2.index(inf)
        print('=' * 70)
        print('{:<20} \t {:>6} \t {:>24.2f}%'.format(copiaBairrosInf[ind], inf, porcenInf[ind]))
        print('=' * 70)
        copiaBairrosInf.pop(ind)
        copiaNumInf2.pop(ind)
        porcenInf.pop(ind)


# Requisito 6:
def taxaCrescimento(paci, semanas):
    # Variáveis que armazenam a quantidade de infectados por semana
    if len(paci) > 0:
        s1 = 0
        s2 = 0
        # Primeiro mês do ano
        primeiroMes = paci.get(1)[5]
        # Último mês do ano
        ultimoMes = paci.get(len(paci))[5]
        # mês
        print('{} \t{}'.format('MES', 'PORCENTAGEM'))
        for i in range(primeiroMes, ultimoMes + 1):
            # semana
            for s in semanas:
                # pacientes
                for k in paci:
                    if paci.get(k)[4] in semanas.get(s) and paci.get(k)[5] == i:
                        s1 += 1
                if s1 >= 0:
                    if s1 > 0:
                        try:
                            porc = ((s1 - s2) / s2) * 100
                        except ZeroDivisionError:
                            porc = ((s1 - s2) / 1) * 100
                        if porc > 0 and s2 == 0:
                            print('{:02}/{:02} : {:>6}'.format(s, i, '----'))
                        elif porc <= 0:
                            print('{:02}/{:02} : {:>5}%'.format(s, i, 0.0))
                        else:
                            print('{:02}/{:02} : {:>5.1f}%'.format(s, i, porc))
                        s2 = s1
                    elif s1 == 0 and s2 > 0:
                        print('{:02}/{:02} : {:>5}%'.format(s, i, 0.0))
                s1 = 0
    else:
        print('\nLista de pacientes vazia')


# Requisito 7:
def percentualMF(paci):
    # variaveis contadoras dos gêneros
    masc = 0
    femi = 0
    for k in paci:
        sexo = paci.get(k)[3]
        # uso de estrutua condicional para contar a quantidade de generos masculinos e femininos
        if sexo == 'M':
            masc += 1
        else:
            femi += 1
    # calculo da porcentagem dos generos em relacao ao total de pacientes
    percMasc = (masc / len(paci)) * 100
    percFemi = (femi / len(paci)) * 100
    print('\nPercentual de Mulheres Infectadas: {:.2f}%'.format(percFemi))
    print('Percentual de Homens Infectados: {:.2f}%'.format(percMasc))


# Requisito 8:
def percentualIdade(paci):
    if len(paci):
        # Lista que recebe a soma de cada idade
        soma = [0, 0, 0, 0, 0, 0]
        # Lista que armazena as porcentagens
        porcIdades = []
        # Lista para representar as idades
        ida = ['0 - 10', '11 - 20', '21 - 40', '41 - 60', '61 - 80', 'mais de 80']
        for k in paci:
            idades = paci.get(k)[1]
            if idades >= 0 and idades <= 10:
                soma[0] = soma[0] + 1
            elif idades >= 11 and idades <= 20:
                soma[1] = soma[1] + 1
            elif idades >= 21 and idades <= 40:
                soma[2] = soma[2] + 1
            elif idades >= 41 and idades <= 60:
                soma[3] = soma[3] + 1
            elif idades >= 61 and idades <= 80:
                soma[4] = soma[4] + 1
            else:
                soma[5] = soma[5] + 1
        for idade in soma:
            porcIdades.append((idade / sum(soma)) * 100)
        print('IDADES (ANOS) \t PORCENTAGEM')
        print('=' * 30)
        for x in range(6):
            print('{:<10} \t \t {:.2f}%'.format(ida[x], porcIdades[x]))
        print('=' * 30)
    else:
        print('faltam pacientes na lista para executar esta função')


# Requisito 9:
def percentualCurados(paci):
    if len(paci) > 0:
        # Variável que recebe a quantidade de pessoas curadas
        quantCurados = 0
        for k in paci:
            if paci.get(k)[7] == 'CURADO':
                quantCurados += 1
        percSalvos = (quantCurados / len(paci)) * 100
        print('\nPercentual de Curados: {:.2f}%'.format(percSalvos))
    else:
        print('Nao ha pacientes cadastrados')


# Requisito 10:
def grafico(paci, semanas):
    primeiroMes = paci.get(1)[5]
    ultimoMes = paci.get(len(paci))[5]
    inf = 0
    inf2 = 0
    contador = list()
    # mês
    for i in range(primeiroMes, ultimoMes + 1):
        # semana
        for s in semanas:
            # pacientes
            for k in paci:
                if paci.get(k)[4] in semanas.get(s) and paci.get(k)[5] == i:
                    inf += 1
            inf = inf + inf2
            contador.append(inf)
            inf2 = inf
            inf = 0
    # Criando semanas e meses
    dias = list()
    for j in range(primeiroMes, ultimoMes + 1):
        for x in range(1, 5):
            texto = str(x) + '/' + str(j)
            dias.append(texto)
    # Criação do gráfico
    plt.xlabel('semana/mes')
    plt.ylabel('quantidade de pacientes')
    plt.plot(dias, contador)
    plt.show()
