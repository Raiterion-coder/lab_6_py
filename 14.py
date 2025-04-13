import threading
import time
import random


class MailServer:
    def __init__(self):
        self.clients = {}
        self.lock = threading.Lock()

    def register_client(self, user):
        with self.lock:
            if user not in self.clients:
                self.clients[user] = []
                print(f"Пользователь {user} зарегистрирован на сервере.")
            else:
                print(f"Пользователь {user} уже зарегистрирован.")

    def receive_mail(self, user):
        with self.lock:
            if user in self.clients:
                if self.clients[user]:
                    message = self.clients[user].pop(0)
                    print(f"Пользователь {user} получил письмо: {message}")
                else:
                    print(f"Нет новых писем для пользователя {user}.")
            else:
                print(f"Пользователь {user} не зарегистрирован.")

    def send_mail(self, sender, recipient, message):
        with self.lock:
            if sender in self.clients and recipient in self.clients:
                self.clients[recipient].append(message)
                print(f"Письмо отправлено от {sender} к {recipient}: {message}")
            else:
                print(f"Не удалось отправить письмо: {sender} или {recipient} не зарегистрирован.")


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.server.register_client(user)

    def receive_mail(self):
        self.server.receive_mail(self.user)

    def send_mail(self, recipient, message):
        self.server.send_mail(self.user, recipient, message)


def client_thread(client):
    while True:
        client.receive_mail()
        time.sleep(random.randint(1, 5))
        recipient = random.choice(["user1", "user2", "user3"])
        message = f"Сообщение от {client.user} для {recipient}"
        client.send_mail(recipient, message)
        time.sleep(random.randint(1, 5))


# Создаем сервер и клиентов
server = MailServer()
client1 = MailClient(server, "user1")
client2 = MailClient(server, "user2")
client3 = MailClient(server, "user3")

# Запускаем клиентов в отдельных потоках
threads = [
    threading.Thread(target=client_thread, args=(client1,)),
    threading.Thread(target=client_thread, args=(client2,)),
    threading.Thread(target=client_thread, args=(client3,))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
