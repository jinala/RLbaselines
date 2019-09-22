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


def arg_parser():
	"""
	Create an empty argparse.ArgumentParser.
	"""
	import argparse
	return argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

def batch_arg_parse():
  parser = arg_parser()
  parser.add_argument('--log_path', help='Directory to save learning curve data.', default="./", type=str)
  parser.add_argument('--env', help="Name of the environment", default="CarRetrievalTrain-v0", type=str)
  return parser

def main(args):
  parser = batch_arg_parse()
  args, unknown_args = parser.parse_known_args(args)
  runjobs(args.env, args.log_path)

'''
Complete n subs, executing at mosmt maxn at once

python batchrun.py num_runs=2 log_path="ok"
'''
def runjobs(env = "CarRetrievalTrain-v0",  log_path = 'myfile', alg = "ppo2", **kwargs):
  

	log_path = path.join(log_path)
	sub_folders = [x[0] for x in os.walk(log_path)][1:]
	print(sub_folders)
	#assert(False)

	for folder in sub_folders:
	
		program =  " python -m baselines.run" + \
				   " --alg={}".format(alg) + \
				   " --env={}".format(env) + \
				   " --num_timesteps={}".format(0) + \
				   " --load_path={}".format(path.join(folder, "model.pkl")) + \
				   " --eval;"
		test_env = copy.copy(env)
		test_env = test_env.replace("Train", "Test")
		program +=  " python -m baselines.run" + \
				   " --alg={}".format(alg) + \
				   " --env={}".format(test_env) + \
				   " --num_timesteps={}".format(0) + \
				   " --load_path={}".format(path.join(folder, "model.pkl")) + \
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

		with open(path.join(folder, "eval.out"), "w") as outfile:
		  res = subprocess.Popen(program, stdout=outfile, stderr=outfile, shell=True)
		  print("Tried to run, got return value {}".format(res))

if __name__ == '__main__':
  main(sys.argv)
