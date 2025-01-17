def calcula_imc(peso, altura):
    try:
        imc = peso / (altura**2)
        
        if imc < 16:
            resultado = "Magreza grave"
        elif 16 <= imc < 17:
            resultado = "Magreza moderada"
        elif 17 <= imc < 18.5:
            resultado = "Magreza leve"
        elif 18.5 <= imc < 25:
            resultado = "Peso ideal"
        elif 25 <= imc < 30:
            resultado = "Sobrepeso"
        elif 30 <= imc < 35:
            resultado = "Obesidade grau I"
        elif 35 <= imc < 40:
            resultado = "Obesidade grau II (severa)"
        elif imc >= 40:
            resultado = "Obesidade grau III (mórbida)"
        else:
            resultado = "Índice não identificado"
            
        return round(imc, 2), resultado
        
    except ZeroDivisionError:
        return None, "Altura não pode ser zero"

def main():
    while True:
        print("\nCalculadora de IMC")
        entrada = input("Digite seu peso (kg) ou 'sair' para encerrar: ")

        if entrada.lower() == 'sair':
            print("Obrigado por utilizar a Calculadora!")
            break
        
        try:
            peso = float(entrada)
            altura = float(input("Digite sua altura (m): "))
            
            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser maiores que zero!")
                continue
                
            imc, resultado = calcula_imc(peso, altura)
            
            if imc is None:
                print(resultado)
            else:
                print(f"\nSeu IMC é {imc}")
                print(f"Classificação: {resultado}")
                
        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
