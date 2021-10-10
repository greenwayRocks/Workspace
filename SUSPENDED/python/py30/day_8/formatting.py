msg_template = '''Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
'''

def format_msg(name='Justin', website='cfe.sh'):
    my_msg = msg_template.format(name=name, website=website)
    return my_msg
