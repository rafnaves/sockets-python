# -*- coding: utf-8 -*-
import socket

def main():
    HOST = "localhost"
    PORT = 6666

    # Criação do socket do servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen(1) 

    print(f"Servidor aguardando conexão em {HOST}:{PORT}...")

    try:
        # Aceitando conexão do cliente
        conexao, endereco = servidor.accept()
        print(f"Cliente conectado: {endereco}")

        numeros = []
        while True:
            try:
                # Recebendo dados do cliente
                dados = conexao.recv(1024).decode("utf-8").strip()
                if not dados:
                    print("Cliente desconectado.")
                    break

                print(f"Dados recebidos: {dados}")

                # Convertendo dados para inteiros
                try:
                    numero = int(dados)
                except ValueError:
                    print("Erro: Dados não são um número inteiro válido.")
                    continue

                # Verificando término da lista
                if numero == -1:
                    break
                numeros.append(numero)

            except ConnectionResetError:
                print("Erro: Conexão foi resetada pelo cliente.")
                break
            except socket.timeout:
                print("Erro: Tempo limite da conexão expirado.")
                break

        if numeros:
            soma = sum(numeros)
            media = soma / len(numeros)
            # Enviando soma para o cliente
            resposta = f"Soma: {soma}\nMédia: {media:.2f}\n"
            conexao.sendall(resposta.encode())
            print(f"Resultado enviado: {resposta.strip()}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        # Encerrando conexão
        print("Encerrando a conexão...")
        conexao.close()
        servidor.close()

if __name__ == "__main__":
    main()
