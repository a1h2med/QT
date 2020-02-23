import os
import subprocess

# this function to upload file with fixed name
def upload_file(port):
    cmd = 'cd'
    cmd2 = 'ampy --port '+port + ' put main.py'
    cdm3 = 'ampy --port '+port + 'get ex.py'
    print(cmd2)
    os.system(cmd2)
    # return os.popen(cmd2).read()
    # return subprocess.check_output(['cd'])


def random_op(port):
    cmd2 = 'ampy --port '+port + ' put test.py'
    print(cmd2)
    os.system(cmd2)


def run_file(port):
    cmd = 'cd'
    cmd2 = 'ampy --port '+port + ' run main.py'
    # cdm3 = 'ampy --port '+port + 'get ex.py'
    print(cmd2)
    # os.system(cmd2)
    return os.popen(cmd2).read()
    # return subprocess.check_output(['cd'])


# this function to create file and store the code entered
def create_file(text):
    f = open("main.py", "w+")
    # x+ x:for write permission and the + sign for create the file if isn't exist
    f.write(text)
    f.close()

command = 'cd'
os.system(command)
# text = input()
# create_file(text)
# upload_file(text)
# run_file(text)
