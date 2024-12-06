# -*- coding: utf-8 -*-

import socket
import time 

# Criação do socket
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketCliente.settimeout(5)  # Define o timeout para 5 segundos

try:
    # Tentativa de conexão
    socketCliente.connect(("localhost", 6666))
    print("Conectado ao servidor.")

    # Envio de mensagem para o servidor
    lista = [4, 5, 89, -1]
    for item in lista:
        mensagem = f"{item}\n"
        socketCliente.sendall(mensagem.encode())
        print(f"Dados enviados: {mensagem.strip()}")
        time.sleep(10)  # Atraso entre os envios

    # Introduzindo atraso para permitir interrupção do servidor
    print("Aguardando para receber a resposta...")
    time.sleep(5)

    # Leitura da resposta
    data = socketCliente.recv(1024)
    print('Resposta: ', data.decode("utf-8"))

except socket.timeout:
    print("Erro: O servidor não respondeu no tempo esperado. Verifique se o endereço IP está correto e acessível.")
except ConnectionRefusedError:
    print("Erro: A conexão foi recusada. O servidor pode estar offline ou a porta pode não estar aberta.")
except BrokenPipeError:
    print("Erro: A conexão foi interrompida enquanto o cliente tentava enviar dados. O servidor foi desconectado abruptamente.")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    # Encerrando a conexão
    print("Fechando a conexão com o servidor.")
    socketCliente.close()
