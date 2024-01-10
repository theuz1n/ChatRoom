import socket
import threading

HOST = "127.0.0.1"
PORT = 50002

class Servidor:
    def __init__(self):
        self.salas = {"1": [], "2": [], "3": []}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(1)
        print(f"Servidor iniciado em {HOST}:{PORT}")

    def iniciar(self):
        while True:
            conexao, endereco = self.socket.accept()
            print(f"Conexão estabelecida com {endereco}")
            cliente_thread = threading.Thread(target=self.lidar_cliente, args=(conexao,))
            cliente_thread.start()

    def lidar_cliente(self, conexao,nome_usuario = None):
        sala = None
        while True:
            mensagem = conexao.recv(1024).decode()

            if not mensagem:
                print(f"Conexão com {nome_usuario} encerrada.")
                break

            

            if not sala:
                opcao = mensagem[0]
                if opcao == "1":
                    if not nome_usuario:
                        print(f"Usuário registrado.")
                        self.enviar_mensagem(conexao, f"Bem-vindo(a), {mensagem}! Escolha uma opção abaixo:")
                        salas_disponiveis = ", ".join(self.salas.keys())
                        self.enviar_mensagem(conexao, f"Salas disponíveis: {salas_disponiveis}")
                elif opcao == "3":
                    num_sala = mensagem[1:]
                    if num_sala not in self.salas:
                        self.enviar_mensagem(conexao, "Sala não existe.")
                    else:
                        sala = num_sala
                        self.salas[sala].append(conexao)
                        self.enviar_mensagem(conexao, f"Você entrou na sala {sala}. Escolha uma opção abaixo:")
                else:
                    self.enviar_mensagem(conexao, "Opção inválida.")
                continue

            if sala:
                opcao = mensagem[0]
                if opcao == "4":
                    print(nome_usuario)
                    usuarios_sala = ", ".join([c.getpeername()[0] for c in self.salas[sala]])
                    self.enviar_mensagem(conexao, f"Usuários na sala: {usuarios_sala,nome_usuario}")
                elif opcao == "5":
                    self.salas[sala].remove(conexao)
                    self.enviar_mensagem(conexao, f"Você saiu da sala {sala}.")
                    sala = None
                else:
                    mensagem = f"{nome_usuario}: {mensagem}"
                    for cliente in self.salas[sala]:
                        if cliente is not conexao:
                            self.enviar_mensagem(cliente, mensagem)

    def enviar_mensagem(self, conexao, mensagem):
        conexao.send(mensagem.encode())
def main():
    servidor = Servidor()
    servidor.iniciar()

    return 0
if __name__ == '__main__':
    main()