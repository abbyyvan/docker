import argparse


parser = argparse.ArgumentParser(
                    prog='Docker_example',
                    description='It takes an argument')
parser.add_argument('-p', '--password')
args = parser.parse_args()

print('password is '+ args.password)
