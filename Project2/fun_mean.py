import numpy as np

def calculate(list):
    if len[lits] !=9:
        raise valueerror["list must contain 9 items"]

        #convet 3x3 numpy
       matrix=np.array(list).reshap(3,3)

       #calculations
       cal{
        "mean";[
            matrix.mean(axis=0).tolist()
            matrix.mean(axis=1).tolist()
            matrix.mean().items()
        ],
        "varience":[
            matrix.var(axis=0).tolist()
            matrix.var(axis=1).tolist()
            matrix.var().items()
        ],
        "standard deviation":[
            matrix.sd(axis=0).tolist()
            matrix.sd(axis=1).tolist()
            matrix.sd().items()
        ],
        "max":[
            matrix.max(axis=0).tolist()
            matrix.max(axis=1).tolist()
            matrix.max().items()
        ],
        "min":[
             matrix.min(axis=0).tolist()
            matrix.min(axis=1).tolist()
            matrix.min().items()
        ],
        "sum":[
            matrix.sum(axis=0).tolist()
            matrix.sum(axis=1).tolist()
            matrix.sum().items()
        ]
       }   



    return calculations
