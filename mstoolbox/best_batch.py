#creating function to be added to package

import matplotlib.pyplot as plt
import matplotlib
from random import randint

def best_batch_plot():
    """Test function for sharing with colleagues"""
    x = []
    y = []
    for i in range(49):
        x.append(randint(1,85))
        y.append(randint(1,90))
    x.append(99)
    y.append(99)
    figure = plt.figure(figsize=(6,4))
    plt.scatter(x,y)
    plt.title("Le Wagon batch 708 is the best")
    plt.xlabel("Looks")
    plt.ylabel("Brains")
    plt.text(94, 92, 'Batch 708')
    matplotlib.pyplot.show(block=True)
    figure.savefig('708.png')
    print("You should have a new image named '708' saved in your directory - please open it!")
    return figure

if __name__ == "__main__":
    print("Le Wagon batch 708...")
    
def state_best_batch():
    best = "Obviously the best batch is 708"
    return best

def where_is_best():
    where = "Our centre is in Shanghai, but we have ppl in Beijing and Hong Kong too!"
    return where