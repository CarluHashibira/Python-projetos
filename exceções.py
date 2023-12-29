# Exceção é um objeto que representa um erro que ocorreu ao executar o programa
# Blocos try ... except

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um numero: '))
            n2 = int(input('Digite um outro numero: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. Tente novamente.')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é dificil dividir por zero!')
    except:
        print(f'Ocorreu um erro desconhecido...')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'\nFim do calculo')


try:
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print(f'Não é dificil dividir por zero!')
