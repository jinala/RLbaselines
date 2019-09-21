import random
import numpy as np

def unif_range(a, b):
    return random.random() * (b - a) + a

def rand_elem(xs):
    return xs[random.randrange(len(xs))]

def rand_int_linspace(start, stop, num = 50):
    return rand_elem([int(x) for x in  np.linspace(start, stop, num)])


def mujoco():
    return dict(
        nsteps=2048,
        nminibatches=32,
        lam=0.95,
        gamma=0.99,
        noptepochs=10,
        log_interval=1,
        ent_coef=0.0,
        lr=lambda f: 3e-4 * f,
        cliprange=0.2,
        value_network='copy'
    )

def atari():
    return dict(
        nsteps=128, nminibatches=4,
        lam=0.95, gamma=0.99, noptepochs=4, log_interval=1,
        ent_coef=.01,
        lr=lambda f : f * 2.5e-4,
        cliprange=0.1,
    )

def retro():
    return atari()

def car_retrieval_train():
    lr = unif_range(0.003, 5e-6)
    return dict(
        # horizon = rand_int_linspace(32, 500),
        nminibatches = rand_elem([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]),
        ent_coef = rand_elem([0.0, 0.01, 0.05, 0.1]),
        noptepochs = rand_int_linspace(3, 36),
        cliprange = rand_elem([0.1, 0.2, 0.3]),
        gamma = 0.99,
        lr = lambda f : f * lr
    )

'''def pendulum_train():
    lr = unif_range(0.003, 5e-6)
    print("lr: ", lr)
    return dict(
        # horizon = rand_int_linspace(32, 500),
        nminibatches = rand_elem([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]),
        ent_coef = rand_elem([0.0, 0.01, 0.05, 0.1]),
        noptepochs = rand_int_linspace(3, 36),
        cliprange = rand_elem([0.1, 0.2, 0.3]),
        gamma = 0.99,
        lr = lambda f : f * lr
    )'''

# best version for pendulum
def pendulum_train():
    lr = 0.0003
    return dict(
        # horizon = rand_int_linspace(32, 500),
        nminibatches = 1,
        ent_coef = 0.01,
        noptepochs = 28,
        cliprange = 0.1,
        gamma = 0.99,
        lr = lambda f : f * lr
    )

def mountain_car_train():
    lr = unif_range(0.003, 5e-6)
    print("lr: ", lr)
    return dict(
        # horizon = rand_int_linspace(32, 500),
        nminibatches = rand_elem([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]),
        ent_coef = rand_elem([0.0, 0.01, 0.05, 0.1]),
        noptepochs = rand_int_linspace(3, 36),
        cliprange = rand_elem([0.1, 0.2, 0.3]),
        gamma = 0.99,
        lr = lambda f : f * lr
    )
