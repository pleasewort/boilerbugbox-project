#second script process ran by image
import subprocess

subprocess.call(["git", "remote", "add", "origin", "https://github.com/pleasewort/boilerbugbox-project"])
subprocess.call(["git", "config", "--global", "user.email", "jonnyopower@gmail.com"])
subprocess.call(["git", "config", "--global", "user.name" ,"pleasewort"])
subprocess.call(["git", "init"])
subprocess.call(["git","pull","origin","main"])
subprocess.call(["git","add","--all","./"])
subprocess.call(["git","commit","-a","-m","all the stuff"])
subprocess.call(["git","push","-f","origin","master:refs/heads/main"])

#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

