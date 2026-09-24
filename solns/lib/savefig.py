def savefig(filename):
    from matplotlib import pyplot as plt

    plt.savefig(f'{filename}.svg', transparent=True)
    plt.savefig(f'{filename}.png')