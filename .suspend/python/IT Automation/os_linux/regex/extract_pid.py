# Extract PID from a logfile
import re


def extract_pid():
    # regex = r"\[(\d+)\]"

    # Reading file
    fp = open('logfile.py', 'r')
    punc = 0
    for index, line in enumerate(fp):
        print('{} - {}'.format(index+1, line).strip())
        result = re.split(r'([.?!, \n])', line)
        # for char in '.?!, ':
        #     if char in [resulty for resulty in result]:
        #         punc += 1
        # print(result + [str(punc)])
        for word in result:
            for char in '.?!, ':
                if char in word.strip():
                    punc += 1
        print(' '.join(result))
    fp.close()
