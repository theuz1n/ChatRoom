#   Chat 

 Este projeto visa criar um  um sistema simples de bate-papo Cliente/Servidor. para os usuários se comunicarem em salas virtuais. Abaixo estão os principais recursos e funcionalidades do servidor e do cliente.

 A aplicação é desenvolvida para trabalhar os seguintes conceitos em python com redes.
-threads 
	-ilimitadas
	 -travas
	 - fila síncronas
	 - framework socketserver
	 - framework Asyncio
	 - framework asyncio - corrotinas

## Servidor

### Registro de Salas

- O servidor mantém o registro de salas disponíveis, organizadas por temas (ex.: Educação, Entretenimento, TI, etc.).
- As salas podem ser fixas .

### Ingresso em Salas

- Permite que os usuários ingressem e saiam de uma sala a qualquer momento.

### Registro de Nickname

- Os usuários podem registrar um nickname no momento em que entram no Chat.
- Cada nickname deve ser único no Chat. Se um nickname já estiver registrado, o sistema solicitará outro nickname.

### Recebimento e Entrega de Mensagens

- Toda comunicação entre clientes é intermediada pelo servidor.
- As mensagens enviadas por um usuário são encaminhadas pelo servidor para os demais participantes da sala.

## Cliente

### Interface

- Cria uma interface amigável para interação com o usuário, podendo ser no modo texto.

### Registro de Nickname

- Solicita que o usuário registre um nickname ao entrar no PyChat.
- Se o nickname já estiver registrado, emite um aviso e solicita outro nickname.

### Salas Disponíveis

- Após o registro, o usuário pode escolher uma sala de bate-papo entre as salas disponíveis no servidor.

### Bate-Papo

- Permite que o usuário envie mensagens e leia mensagens dos participantes da sala.
- O comando "/sair" permite que o usuário saia da sala, exibindo um aviso para os demais usuários.
