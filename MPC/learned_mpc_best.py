import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    to_input('input', name='InputData'),

    to_SoftMax("inputVector", 108, offset="(0,0,0)", to="(0,0,0)", height=1, depth=34, width=1, caption='in vector'),
    to_connection("-3,0,0", "inputVector"),

    to_FulCon("fc1", 192, 1, offset="(3,0,0)", to="(inputVector-west)", height=1, depth=60, width=1, caption='ELU()'),
    to_connection("inputVector", "fc1"),

    to_FulCon("fc2", 128, 1, offset="(3,0,0)", to="(fc1-west)", height=1, depth=40, width=1, caption='velocity'),
    to_connection("fc1", "fc2"),

    to_FulCon("fc3", 64, 1, offset="(3,0,0)", to="(fc2-west)", height=1, depth=20, width=1, caption='FC0 1 2'),
    to_connection("fc2", "fc3"),

    to_FulCon("fc4", 32, 1, offset="(3,0,0)", to="(fc3-west)", height=1, depth=10, width=1, caption='FC3 4 5'),
    to_connection("fc3", "fc4"),

    to_FulCon("fc5", 3, 1, offset="(3,0,0)", to="(fc4-west)", height=1, depth=3, width=1, caption='Id()'),
    to_connection("fc4", "fc5"),

    to_SoftMax("outputVel", 3, offset="(2,0,0)", to="(fc5-west)", height=1, depth=3, width=1, caption='out'),
    to_connection("fc5", "outputVel"),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
