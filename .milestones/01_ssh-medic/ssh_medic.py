# SSH medic v1.0
import click
import os
import stat

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


@main.command(hidden=True)
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())


@main.command()
def check():
    ssh_dir = os.path.expanduser('~/.ssh')
    files = [ssh_dir] + os.listdir(ssh_dir)
    to_change = []

    for _file in files:
        path = os.path.join(ssh_dir, _file)
        file_stat = os.stat(path)
        perm = oct(file_stat.st_mode)[-3:]

        # Display Permissions
        click.secho('{:>20} -> {}'.format(_file, perm), fg='yellow', bold=True)

        # Expected Permissions
        priv_perm = '600'
        pub_perm = '644'
        expected = {
            ssh_dir: '700',
            'config': pub_perm,
            'known_hosts': pub_perm,
            'authorized_keys': pub_perm
        }

        # Comparing perms
        # Include private and public key files too!
        if _file.endswith('.pub'):
            expected[_file] = pub_perm

        try:
            expected_perm = expected[_file]
        except KeyError:
            expected[_file] = priv_perm
            expected_perm = expected[_file]

        if expected_perm != perm:
            click.echo('{} has {}, should be {}!'.format(
                _file, perm, expected_perm))
            to_change.append((_file, perm, expected_perm))

    if to_change:
        return to_change
    else:
        return ''


@main.command()
@click.pass_context
def fix(ctx):
    click.secho(f"{'-- FIX Operation --':>20}",
                fg='red', bold=True, underline=True)
    data = ctx.invoke(check)

    for _file, perm, new_perm in data:
        click.secho("Changing {}'s {} perm to {}".format(
            _file, perm, new_perm), bold=True)


if __name__ == '__main__':
    main()
