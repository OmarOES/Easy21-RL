from easy21_env import ACTIONS
import numpy as np


def get_Q(Q, state, action):
    return Q[state.dealer_card-1, state.player_sum-1, action]


def get_epsilon(N0, Ns, state):
    return N0 / (N0 + Ns[state.dealer_card-1, state.player_sum-1])


def epsilon_greedy_policy(epsilon, Q, state):
    rand = np.random.rand()
    print("rand: " + str(rand) + " epsilon: " + str(epsilon))
    if (rand > epsilon):
        return np.argmax(Q[state.dealer_card-1, state.player_sum-1, :])
    else:
        return np.random.choice(ACTIONS)

# ------------------------------------


import matplotlib
matplotlib.use("TkAgg")

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, rc
# rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
# rc('text', usetex=True)
import matplotlib.pyplot as plt

import numpy as np
from pprint import pprint


def create_surf_plot(X, Y, Z, fig_idx=1):
    fig = plt.figure(fig_idx)
    ax = fig.add_subplot(111, projection="3d")

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    # surf = ax.plot_wireframe(X, Y, Z)

    return surf


DEALER_RANGE = range(1, 11)
PLAYER_RANGE = range(1, 22)


def plot_V(Q, save=None, fig_idx=0):
    V = np.max(Q, axis=2)
    X, Y = np.mgrid[DEALER_RANGE, PLAYER_RANGE]

    surf = create_surf_plot(X, Y, V)

    plt.title("V*")
    plt.ylabel('player sum', size=18)
    plt.xlabel('dealer', size=18)

    if save is not None:
        plt.savefig(save, format='pdf', transparent=True)
    else:
        plt.show()

    plt.clf()