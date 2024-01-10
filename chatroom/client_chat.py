import socket
import threading

HOST = "127.0.0.1"
PORT = 50002

class Cliente:
    def __init__(self, nome_usuario):
        self.nome_usuario = nome_usuario
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST,PORT))

        self.receber_mensagens_thread = threading.Thread(target=self.receber_mensagens)
        self.receber_mensagens_thread.start()

    def receber_mensagens(self):
        while True:
            mensagem = self.socket.recv(1024).decode()
            print(mensagem)

    def enviar_mensagem(self, mensagem, destinatario=None):
        if destinatario:
            mensagem = f"{self.nome_usuario} -> {destinatario}: {mensagem}"
        else:
            mensagem = f"{self.nome_usuario}: {mensagem}"
        self.socket.send(mensagem.encode())

    def iniciar(self):
        opcao = ""
        while opcao != "4":
            opcao = input("Opcoes disponiveis:\n1 - Listar salas disponiveis\n2 - Entrar em uma sala\n3 - Sair da sala\n4 - Sair do chat\nDigite a opcao desejada:  ")
            if opcao == "1":
                self.socket.send("1".encode())
            elif opcao == "2":
                num_sala = input("Digite o número da sala desejada: ")
                self.socket.send(f"3{num_sala}".encode())
                while True:
                    opcao_sala = input("Opções disponíveis:\n1 - Enviar mensagem\n2 - Listar usuários\n3 - Sair da sala\nDigite a opção desejada: ")
                    if opcao_sala == "1":
                        mensagem = input("Digite a mensagem a ser enviada: ")
                        destinatario = input("Digite o nome do destinatário (ou deixe em branco para enviar para todos): ")
                        self.enviar_mensagem(mensagem, destinatario)
                    elif opcao_sala == "2":
                        self.socket.send("4".encode())
                        mensagem = self.socket.recv(1024).decode()
                        print(mensagem)
                        
                    elif opcao_sala == "3":
                        self.socket.send("5".encode())
                        break
            elif opcao == "3":
                self.socket.send("6".encode())
                self.socket.close()
                break
            elif opcao == "4":
                self.socket.close()
def main():
    
    nome_usuario = input(b"Digite seu nome de usuario: ")
    cliente = Cliente(nome_usuario)
    cliente.iniciar()

if __name__ == '__main__':
    main()