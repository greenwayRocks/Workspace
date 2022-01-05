#!/usr/bin/env python3

import os
import re
import csv


def contains_domain(address, domain):
    domain = r'[\w\.-]+@' + domain + '$'
    if re.match(domain, address):
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    old_domain = r'' + old_domain + '$'
    new_addr = re.sub(old_domain, new_domain, address)
    return new_addr

def main():
    '''
    Process list of emails, update with new domains.
    '''
    old_domain, new_domain = 'yahoo.com', 'gmail.com'
    csv_file = os.path.expanduser('~/data/user_emails.csv')
    report_file = os.path.expanduser('~/data/updated_emails.csv')
    
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file, 'r') as fp:
        user_data_list = list(csv.reader(fp))
        user_email_list = [row[1].strip() for row in user_data_list[1:]]
        
        for email in user_email_list:
            if contains_domain(email, old_domain):
                old_domain_email_list.append(email)
                new_email = replace_domain(email, old_domain, new_domain)
                new_domain_email_list.append(new_email)

        email_key = 'Email'
        email_index = user_data_list[0].index(email_key)

        for row in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if row[email_index] == old_domain:
                    row[email_index] = new_domain
        fp.close()
        
    with open(report_file, 'w+') as output:
        writer = csv.writer(output)
        writer.writerows(user_data_list)
        output.close()

if __name__ == '__main__':
    main()
