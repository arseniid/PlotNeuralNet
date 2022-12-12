import sys
sys.path.append('../../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '../..' ),
    to_cor(),
    to_begin(),

    to_SoftMax("inputVector", 108, offset="(0,0,0)", to="(0,0,0)", height=1, depth=25, width=1, caption='in vector'),

    to_FulCon("fc0", 192, 1, offset="(2,0,0)", to="(inputVector-west)", height=1, depth=45, width=1, caption='non-linearity'),
    to_connection("inputVector", "fc0"),
    to_BN("bn0", offset="(1.5,0,0)", to="(fc0-west)", height=1, depth=45, width=1, caption="BatchNorm1d0"),
    to_connection("fc0", "bn0"),

    to_FulCon("fc1", 128, 1, offset="(3,0,0)", to="(bn0-west)", height=1, depth=30, width=1, caption='velocity'),
    to_connection("bn0", "fc1"),
    to_BN("bn1", offset="(1.5,0,0)", to="(fc1-west)", height=1, depth=30, width=1, caption="BatchNorm1d1"),
    to_connection("fc1", "bn1"),

    to_FulCon("fc2", 64, 1, offset="(3,0,0)", to="(bn1-west)", height=1, depth=15, width=1, caption='Id()'),
    to_connection("bn1", "fc2"),
    to_BN("bn2", offset="(1.5,0,0)", to="(fc2-west)", height=1, depth=15, width=1, caption="BatchNorm1d2"),
    to_connection("fc2", "bn2"),

    to_FulCon("fc3", 32, 1, offset="(3,0,0)", to="(bn2-west)", height=1, depth=12, width=1, caption='FC0 1'),
    to_connection("bn2", "fc3"),
    to_BN("bn3", offset="(1.5,0,0)", to="(fc3-west)", height=1, depth=11, width=1, caption="FC2 3"),
    to_connection("fc3", "bn3"),

    to_FulCon("fc4", 3, 1, offset="(3,0,0)", to="(bn3-west)", height=1, depth=3, width=1, caption='FC4 5'),
    to_connection("bn3", "fc4"),

    to_SoftMax("outputVel", 3, offset="(2,0,0)", to="(fc4-west)", height=1, depth=3, width=1, caption='out'),
    to_connection("fc4", "outputVel"),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
