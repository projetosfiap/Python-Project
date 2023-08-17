from funcoes import *

nome_cliente = input("Digite o seu nome e sobrenome: ")
print("Olá {}. Como posso te ajudar?".format(nome_cliente))


while True:
    print("1 - Solicitar um guincho")
    print("2- Falar com um atendente")

    opcoes_inicio = input("Digite uma opção: ")

    if opcoes_inicio == "2":
        numeros_porto()
        break

    elif opcoes_inicio == "1":
        while True:
            print("1 - Caminhão")
            print("2 - Ônibus")
            print("3 - Carreta")
            print("4 - Motorhome")
            opcoes_veiculos = int(input("Digite o número correspondente ao seu veículo: "))

            if opcoes_veiculos == 1 or opcoes_veiculos == 3:
                print("1 - Carga Viva")
                print("2 - Carga Perecível")
                print("3 - Carga Granel")
                print("4 - Carga Perigosa")
                print("5 - Carga Seca")

                while True:
                    opcoes_carga = int(input("Digite o número correspondente à carga do veículo: "))

                    if opcoes_carga == 1:
                        veiculo_caminhao_cargaviva()
                        break

                    elif opcoes_carga == 2:
                        print("1 - Frutas e Legumes")
                        print("2 - Congelados")
                        opcoes_carga_perecivel = int(input("Digite o número correspondente à carga perecível: "))
                        if opcoes_carga_perecivel == 1:
                            veiculo_caminhao_perecivel1()
                            break
                        elif opcoes_carga_perecivel == 1:
                            veiculo_caminhao_perecivel2()
                            break
                        else:
                            opcao_invalida()

                    elif opcoes_carga == 3:
                        veiculo_caminhao_granel()
                        print("1 - Líquido")
                        print("2 - Sólido")
                        while True:
                            opcoes_carga_granel = int(input("Digite o número correspondente à carga granel: "))
                            if opcoes_carga_granel == 1:
                                veiculo_caminhao_granel1()
                                break
                            elif opcoes_carga_granel == 2:
                                veiculo_caminhao_granel2()
                                break
                            else:
                                opcao_invalida()
                            break

                    elif opcoes_carga == 4:
                        veiculo_caminhao_perigoso()
                        print("1 - Explosiva")
                        print("2 - Gases Inflamáveis")
                        print("3 - Líquidos Inflamáveis")
                        print("4 - Substância Perigosa Diversa")
                        while True:
                            opcoes_carga_perigosa = int(input("Digite o número correspondente à carga perigosa: "))

                            if opcoes_carga_perigosa == 1:
                                print("Sua carga é explosiva")
                                break

                            elif opcoes_carga_perigosa == 2:
                                print("Sua carga contém gases inflamáveis.")
                                break

                            elif opcoes_carga_perigosa == 3:
                                print("Sua carga contém líquidos tóxicos.")
                                break

                            elif opcoes_carga_perigosa == 4:
                                opcoes_carga_perigosa_diversa = input("Especifique o tipo de carga: ")
                                break

                            else:
                                opcao_invalida()
                        break

                    else:
                        opcao_invalida()
                break

            elif opcoes_veiculos == 2:
                print("1 - Articulado")
                print("2 - Convencional")
                print("3 - Executivo")
                print("4 - Outro")
                while True:
                    opcoes_veiculos_onibus = input("Digite o número correspondente ao seu ônibus: ")

                    if opcoes_veiculos_onibus == "1":
                        print("O seu ônibus é articulado, categoria tarifária 60 ou 61.")
                        funcao_continue()
                        break

                    elif opcoes_veiculos_onibus == "2":
                        print("1 - Veículo Escolar")
                        print("2 - Lotação Urbana")
                        print("3 - Ônibus e Microonibus com cobrança de frete")
                        while True:
                            tipos_onibus_convencional = int(input("Digite o número correspondente ao seu veículo: "))

                            if tipos_onibus_convencional == 1:
                                print("Você está com um veículo de transporte escolar. Categoria Tarifária 84 ou 85.")
                                funcao_continue()
                                break

                            elif tipos_onibus_convencional == 2:
                                print("Você está com um veículo convencional de transporte urbano. Categoria tarifária 60 ou 61.")
                                funcao_continue()
                                break

                            elif tipos_onibus_convencional == 3:
                                print("Você está com um veículo convencional de cobrança de frete. Categoria tarifária 58 ou 59.")
                                funcao_continue()
                                break
                            else:
                                opcao_invalida()

                    elif opcoes_veiculos_onibus == "3":
                        print("O seu ônibus é o modelo Executivo. Categoria tarifária de 58 ou 59.")
                        funcao_continue()
                        break

                    elif opcoes_veiculos_onibus == "4":
                        print()
                        opcao5_onibus = input("DIGITE O MODELO DO ÔNIBUS: ")
                        print()
                        break

                    else:
                        opcao_invalida()

                break

            else:
                opcao_invalida()
        break

    else:
        opcao_invalida()

print("\n**** VOCÊ ESTÁ SENDO DIRECIONADO À ETAPA SOBRE AS CONDIÇÕES DA VIA ****\n")

while True:
    print("1 - SIM")
    print("2 - NÃO")
    tombamento_veiculo= int(input("O seu veículo está tombado? "))

    if tombamento_veiculo == 1:
        print("----Enviaremos um Guincho Lança para destombamento e remoção do seu veículo----\n")
        break

    elif tombamento_veiculo == 2:
        print("----Enviaremos um Guincho Lança para a remoção do seu veículo----\n")
        break

    else:
        opcao_invalida()


while True:
    print("1 - SIM")
    print("2 - NÃO")
    acesso_via = int(input("A via apresenta alguma restrição de acesso para que o veículo de guincho chegue até você? "))

    if acesso_via == 1:
        acesso_via_positivo = input("Descreva o local em que você está: ")
        print("Agradecemos as informações. Dentro de instantes, um funcionário credenciado da Porto Seguro irá ate você.")
        print("ATÉ LOGO!")
        break

    if acesso_via == 2:
        print("----Enviaremos um Guincho Lança para a remoção do seu veículo----")
        print("Agradecemos as informações. Dentro de instantes, um funcionário credenciado da Porto Seguro irá ate você.")
        print("ATÉ LOGO!")
        break

    else:
        opcao_invalida()





