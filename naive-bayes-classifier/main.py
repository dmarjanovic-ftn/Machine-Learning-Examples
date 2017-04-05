from bayes import naive_bayes_classifier

"""
    Train data from Tom Mitchell's Book
    
    Day     Outlook     Temperature     Humidity        Wind        Play_Tennis
    ---------------------------------------------------------------------------
    1       Sunny       Hot             High            Weak        No
    2       Sunny       Hot             High            Strong      No
    3       Overcast    Hot             High            Weak        Yes
    4       Rain        Mild            High            Weak        Yes
    5       Rain        Cool            Normal          Weak        Yes
    6       Rain        Cool            Normal          Strong      No
    7       Overcast    Cool            Normal          Strong      Yes
    8       Sunny       Mild            High            Weak        No
    9       Sunny       Cool            Normal          Weak        Yes
    10      Rain        Mild            Normal          Weak        Yes
    11      Sunny       Mild            Normal          Strong      Yes
    12      Overcast    Mild            High            Strong      Yes
    13      Overcast    Hot             Normal          Weak        Yes
    14      Rain        Mild            High            Strong      No
    
"""
if __name__ == "__main__":

    X = [
        ['Sunny',    'Hot',  'High',    'Weak'   ],
        ['Sunny',    'Hot',  'High',    'Strong' ],
        ['Overcast', 'Hot',  'High',    'Weak'   ],
        ['Rain',     'Mild', 'High',    'Weak'   ],
        ['Rain',     'Cool', 'Normal',  'Weak'   ],
        ['Rain',     'Cool', 'Normal',  'Strong' ],
        ['Overcast', 'Cool', 'Normal',  'Strong' ],
        ['Sunny',    'Mild', 'High',    'Weak'   ],
        ['Sunny',    'Cool', 'Normal',  'Weak'   ],
        ['Rain',     'Mild', 'Normal',  'Weak'   ],
        ['Sunny',    'Mild', 'Normal',  'Strong' ],
        ['Overcast', 'Mild', 'High',    'Strong' ],
        ['Overcast', 'Hot',  'Normal',  'Weak'   ],
        ['Rain',     'Mild', 'High',    'Strong' ],
    ]

    D = [
        'No',
        'No',
        'Yes',
        'Yes',
        'Yes',
        'No',
        'Yes',
        'No',
        'Yes',
        'Yes',
        'Yes',
        'Yes',
        'Yes',
        'No'
    ]

    input = ['Sunny', 'Cool', 'High', 'Strong']

    hypotheses = ['Yes', 'No']

    naive_bayes_classifier(input, hypotheses, X, D)