import sys
# import baselines
import subprocess
import argparse
from pdb import set_trace
from os import path
import string
import random
import os

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
  return parser

def main(args):
  parser = batch_arg_parse()
  args, unknown_args = parser.parse_known_args(args)
  runjobs(args.num_runs, args.log_path)

'''
Complete n subs, executing at mosmt maxn at once

python -m baselines.run --alg=ppo2 --env=CarRetrievalTrain-v0 --num_timesteps=1e6
logs to logfile
'''
def runjobs(num_runs = 2, log_path = 'myfile', alg = "ppo2", env = "CarRetrievalTrain-v0", num_timesteps="1e6", **kwargs):
  for i in range(num_runs):
    rnd_str = random_string(5)
    # set_trace()
    run_log_path = path.join(log_path, rnd_str)
    os.mkdir(run_log_path)
    print("Saving to {}".format(run_log_path))
    program = ["python", "-m", "baselines.run",
               "alg={}".format(alg),
               "env={}".format(env),
               "num_timesteps={}".format(num_timesteps),
               "log_path={}".format(run_log_path),
               "save_path={}".format(run_log_path)]

    with open(path.join(run_log_path, "std.out"), "w") as outfile:
      res = subprocess.Popen(program, stdout=outfile, stderr=outfile)
      print("Tried to run, got return value {}".format(res))

if __name__ == '__main__':
  main(sys.argv)
