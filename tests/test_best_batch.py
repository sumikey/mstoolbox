from mstoolbox.best_batch import best_batch_plot
from mstoolbox.best_batch import state_best_batch
from mstoolbox.best_batch import where_is_best

import matplotlib

def test_best_batch_plot():
    assert type(best_batch_plot()) == matplotlib.figure.Figure

def test_state_best_batch():
    assert type(state_best_batch()) == type('best')
    
def test_where_is_best():
    assert type(where_is_best()) == type('best')