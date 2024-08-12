while True:
    print ("Operações disponiveis.");
    print ("1 - Soma.");
    print ("2 - Subtração.");
    print ("3 - Multiplicação.");
    print ("4 - Divisão");
    print ("5 - Sair")
    print ();

    escolha = int(input("Selecione a operação desejada: "));

    if escolha not in [1, 2, 3, 4, 5]:
        print("Opção invalida.");
        continue
        
    elif escolha == 5:
        print("Encerrando calculadora...")
        break
    else:
        num1 = float(input("Digite o primeiro número: "));
        num2 =  float(input("Digite o segundo número: "));

        if escolha == 1:
            print("Resultado: ", num1 + num2);
        elif escolha == 2:
            print("Resultado: ", num1 - num2);
        elif escolha == 3:
            print("Resultado: ", num1 * num2);
        elif escolha == 4:
            print("Resultado: ", num1 / num2);
        else:
            print("Opção invalida.")
    
        repetir = input("\nQuer realizar outra operação? (s/n): ").lower()
        if repetir != 's':
            print("Encerrando...")
            break