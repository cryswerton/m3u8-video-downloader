import os

actual_directory = os.getcwd()
path = os.path.join(actual_directory, 'm3u8-downloader.sh')
cmd = ''
home_path = os.environ.get('HOME') # /home/username
bash_aliases_path = os.path.join(home_path, '.bash_aliases') # /home/username/.bash_aliases
file = ''
alias = f'alias m3u8-get="{path}"'

# create the .bash_aliases file if it doesn't exist
if os.path.exists(bash_aliases_path):
    print(f'{os.path.basename(bash_aliases_path)} already exists in {bash_aliases_path}.')
else:
    file = bash_aliases_path
    open(file, 'a').close()
    print(f'{os.path.basename(bash_aliases_path)} created in {bash_aliases_path}.')

cmd = 'chmod +x m3u8-downloader.sh'
os.system(cmd)
print(f'Given permission to the m3u8-downloader.sh file')

# check if the alias is in the .bash_aliases file.
f = open(bash_aliases_path)
if(alias in f.read()):
    print("alias already exists in the .bash_aliases file.")
    f.close()
else:
    # create an alias in the .bash_aliases file.
    f = open(bash_aliases_path, "a")
    f.write(f'{alias}\n')
    f.close()
    print('Alias created in the .bash_aliases file.')

print('Exit and open the terminal to see the changes.')
