import moduloALP

# pacientes = dict()
pacientes = {1: ['JOÃO BEZERRA DE SOUZA NETO', 26, 'CENTRO', 'M', 4, 2, 'POSITIVO-IGMIGG', 'ISOLAMENTO DOMICILIAR'], 2: ['KARLA ALMEIDA SOUSA', 12, 'JARDIM OÁSIS', 'F', 9, 2, 'POSITIVO-SWAB', 'INTERNADO'],
             3: ['FRANCISCA SILVA DO NASCIMENTO', 10, 'CENTRO', 'F', 10, 2, 'POSITIVO-IGG', 'CURADO'], 4: ['EDNALDO PEREIRA MATOS', 45, 'PIO DOSE', 'M', 15, 2, 'POSITIVO-SWAB', 'OBITO']}
resultado = moduloALP.testeOpcoes()
condicao = moduloALP.statusPacientes()
semanal = moduloALP.gerarSemanas()

while True:
    moduloALP.menu()
    opcao = int(input('Digite uma das opcoes do menu '))
    if opcao == 0:
        break
    elif opcao == 1:
        moduloALP.cadastraPessoa(pacientes, resultado)
    elif opcao == 2:
        moduloALP.listar(pacientes)
    elif opcao == 3:
        moduloALP.inserirStatus(pacientes, condicao)
    elif opcao == 4:
        moduloALP.listarPorStatus(pacientes, condicao)
    elif opcao == 5:
        moduloALP.calcularBairro(pacientes)
    elif opcao == 6:
        moduloALP.taxaCrescimento(pacientes, semanal)
    elif opcao == 7:
        moduloALP.percentualMF(pacientes)
    elif opcao == 8:
        moduloALP.percentualIdade(pacientes)
    elif opcao == 9:
        moduloALP.percentualCurados(pacientes)
    elif opcao == 10:
        moduloALP.grafico(pacientes, semanal)
    else:
        print('\nDigito invalido. Insira uma das opcoes do menu')
print('\nPrograma Encerrado')