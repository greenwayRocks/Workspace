import os

my_dir = '/media/workspace/rename_pro'

os.chdir(my_dir)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_planet, f_title, f_num = [text.strip() for text in f_name.split('-')]
    f_num = f_num[1:].zfill(2)
    new_name = '{}-{}{}'.format(f_num, f_planet, f_ext)
    os.rename(f, new_name)
