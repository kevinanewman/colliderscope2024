import multiprocessing

# import omega_model
from colliderscopeui import run_colliderscope

# fix for for pyinstaller multiprocessing issue
multiprocessing.freeze_support()

run_colliderscope()
