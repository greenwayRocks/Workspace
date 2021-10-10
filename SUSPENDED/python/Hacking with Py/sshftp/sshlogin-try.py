import pexpect
import click

PROMPT = ['# ', '>> ', '> ', '$ ']


def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print((child.before).decode('utf-8', 'ignore'))


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting? '
    connStr = 'ssh ' + str(user) + '@' + str(host)
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error Connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child


@click.command()
@click.argument('host')
@click.option('--user', default='root', help='SSH user')
@click.option('--password', prompt=True, hide_input=True, help='Login password')
@click.option('--cmd', default='ls;ps', help='Command to launch')
def main(host, user, password, cmd):
    child = connect(user, host, password)
    send_command(child, cmd)


if __name__ == '__main__':
    main()
