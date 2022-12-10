import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    to_input('input', name='InputData'),

    to_FulCon("fc0", 156, 1, offset="(-0.5,0,0)", to="(0,0,0)", height=1, depth=18, width=1, caption='shared\_net (Id)'),
    to_connection("-3,0,0", "fc0"),

    to_FulCon("fc1", 256, 1, offset="(3,4,0)", to="(fc0-west)", height=1, depth=30, width=1, caption='Tanh()'),
    to_connection("fc0", "fc1"),
    to_FulCon("fc2", 256, 1, offset="(3,0,0)", to="(fc1-west)", height=1, depth=30, width=1, caption='policy\_net'),
    to_connection("fc1", "fc2"),

    to_FulCon("fc3", 512, 1, offset="(1.5,-2,0)", to="(fc0-west)", height=1, depth=60, width=1, caption='ReLU()'),
    to_connection("fc0", "fc3"),
    to_FulCon("fc4", 512, 1, offset="(3,0,0)", to="(fc3-west)", height=1, depth=60, width=1, caption='mlp\_extractor'),
    to_connection("fc3", "fc4"),

    to_FulCon("fc5", 4, 1, offset="(3,0,0)", to="(fc2-west)", height=1, depth=4, width=1, caption='action\_net'),
    to_connection("fc2", "fc5"),

    to_FulCon("fc6", 1, 1, offset="(4.5,0,0)", to="(fc4-west)", height=1, depth=1, width=1, caption='value\_net'),
    to_connection("fc4", "fc6"),

    to_SoftMax("outputAct", 4, offset="(2,0,0)", to="(fc5-west)", height=1, depth=4, width=1, caption="out action"),
    to_connection("fc5", "outputAct"),

    to_SoftMax("outputVal", 1, offset="(2,0,0)", to="(fc6-west)", height=1, depth=1, width=1, caption="out value"),
    to_connection("fc6", "outputVal"),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
