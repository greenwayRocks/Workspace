import random
import click


class Server:
    def __init__(self):
        self.connections = {}

    def add_connection(self, connection_id):
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        del self.connections[connection_id]

    def load(self):
        total = 0
        for connection_load in self.connections.values():
            total += connection_load
        return total

    def __str__(self):
        return '{:.2f}'.format(self.load())


class LoadBalancing:
    def __init__(self):
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        self.ensure_availability()
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)

    def close_connection(self, connection_id):
        server = self.connections[connection_id]
        server.close_connection(connection_id)
        del self.connections[connection_id]

    def avg_load(self):
        total = 0
        n = len(self.servers)
        for server in self.servers:
            total += server.load()
        return total

    def ensure_availability(self):
        if self.avg_load() > 20:
            self.servers.append(Server())

    def __str__(self):
        loads = [str(server.load()) for server in self.servers]
        return '[{}]'.format(', '.join(loads))


@click.command()
def main():
    '''
    Your load balancer initially has 1 server and spins up a new one if avg_load exceeds 20.
    '''
    l = LoadBalancing()
    click.secho('[[Type [DONE] to exit...]]', fg='red', bold=True)
    # Interactive Session
    while True:
        click.secho('[+] Add a new connection(id): ', fg='white', bg='blue')
        connection_id = input()
        if connection_id == 'DONE':
            break
        if connection_id.startswith('+'):
            temp = int(connection_id[1:])
            for connection in range(temp):
                l.add_connection(connection)
        else:
            l.add_connection(connection_id)
        click.secho('[*] Average Load currently: {:.4f} and servers: {}'.format(
            l.avg_load(), len(l.servers)), fg='white', bg='red')


if __name__ == '__main__':
    main()
