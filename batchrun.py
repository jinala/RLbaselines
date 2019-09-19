import sys
# import baselines
import subprocess

'''
Complete n subs, executing at mosmt maxn at once

python -m baselines.run --alg=ppo2 --env=CarRetrievalTrain-v0 --num_timesteps=1e6
logs to logfile
'''
def main(n = 2, logfile = 'myfile', alg = "ppo2", env = "CarRetrievalTrain-v0", num_timesteps="1e6", **kwargs):
  # savae --save_path
  # log_path

  program = ["python", "-m", "baselines.run", "alg={}".format(alg),
             "env={}".format{env}, "num_timesteps={}".format{num_timesteps}]
  for i in range(n):
    with open(logfile, "w") as outfile:
      res = subprocess.Popen(program, stdout=outfile)
      print("Tried to run, got return value {}".format(res))

if __name__ == '__main__':
  main(sys.argv)
