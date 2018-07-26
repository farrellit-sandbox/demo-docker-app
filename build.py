# will shell out for now 
import re, os, subprocess, sys

for i in os.environ.get("ExtraENV","").split(","):
  res = i.split("=",1)
  var = res[0]
  val = res[1].strip('"')
  os.environ[var] = val

loginproc = subprocess.check_call( [ "sh", "-c", 
  "aws --region {region} ecr get-login --no-include-email | sh".format(region=os.environ['REGION']) 
])

if len(os.environ['Source']):
  sys.stdout.write("Pulling source image '{source}'\n".format(source=os.environ['Source']))
  subprocess.check_call(["docker","pull",os.environ['Source']])
  subprocess.check_call(["docker","tag", os.environ['Source'], os.environ['Target']])
else:
  cmd= ["docker","build","-t",os.environ['Target'] ]
  if os.environ.get('Dockerfile'):
    cmd.extend(["-f",os.environ['Dockerfile']])
  cmd.extend([os.environ.get('DockerDir','.')])
  sys.stdout.write("Building image for '{target}'\n".format(target=os.environ['Target']))
  subprocess.check_call(cmd)

sys.stdout.write("Pushing target image '{target}'\n".format(target=os.environ['Target']))
subprocess.check_call(["docker","push",os.environ['Target']])
