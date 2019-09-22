import sys
# import baselines
import subprocess
import argparse
from pdb import set_trace
from os import path
import string
import random
import os
import copy 

# Random string of length
def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def arg_parser():
    """
    Create an empty argparse.ArgumentParser.
    """
    import argparse
    return argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

def batch_arg_parse():
  parser = arg_parser()
  parser.add_argument('--num_runs', help='Number ofruns ', default=1, type=int)
  parser.add_argument('--log_path', help='Directory to save learning curve data.', default="./", type=str)
  parser.add_argument('--env', help="Name of the environment", default="CarRetrievalTrain-v0", type=str)
  parser.add_argument('--num_timesteps', help="Number of timesteps to train for", default=1e6, type = float )
  return parser

def main(args):
  parser = batch_arg_parse()
  args, unknown_args = parser.parse_known_args(args)
  runjobs(args.env, args.num_runs, args.log_path, args.num_timesteps)

'''
Complete n subs, executing at mosmt maxn at once

python batchrun.py num_runs=2 log_path="ok"
'''
def runjobs(env = "CarRetrievalTrain-v0", num_runs = 2, log_path = 'myfile', num_timesteps="1e6", alg = "ppo2", **kwargs):
  for i in range(num_runs):
    rnd_str = random_string(5)
    # set_trace()
    run_log_path = path.join(log_path, rnd_str)
    os.mkdir(run_log_path)
    print("Saving to {}".format(run_log_path))
    program = "python -m baselines.run" + \
               " --alg={}".format(alg) + \
               " --env={}".format(env) + \
               " --num_timesteps={}".format(num_timesteps) + \
               " --log_path={}".format(run_log_path) + \
               " --save_path={}".format(path.join(run_log_path, "model.pkl;"))
    program +=  " python -m baselines.run" + \
               " --alg={}".format(alg) + \
               " --env={}".format(env) + \
               " --num_timesteps={}".format(0) + \
               " --load_path={}".format(path.join(run_log_path, "model.pkl")) + \
               " --eval;"
    test_env = copy.copy(env)
    test_env = test_env.replace("Train", "Test")
    program +=  " python -m baselines.run" + \
               " --alg={}".format(alg) + \
               " --env={}".format(test_env) + \
               " --num_timesteps={}".format(0) + \
               " --load_path={}".format(path.join(run_log_path, "model.pkl")) + \
               " --eval;"
    '''test_env_v1 = copy.copy(test_env)
    test_env_v1 = test_env_v1.replace("v0", "v1")
    program +=  " python -m baselines.run" + \
               " --alg={}".format(alg) + \
               " --env={}".format(test_env_v1) + \
               " --num_timesteps={}".format(0) + \
               " --load_path={}".format(path.join(run_log_path, "model.pkl")) + \
               " --eval"'''

    #print(env)

    print(program)

    with open(path.join(run_log_path, "std.out"), "w") as outfile:
      res = subprocess.Popen(program, stdout=outfile, stderr=outfile, shell=True)
      print("Tried to run, got return value {}".format(res))

if __name__ == '__main__':
  main(sys.argv)
