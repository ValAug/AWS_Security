# AWS_Booster_Project_2020

*Automating AWS deployment with Python + Boto3*

# Covid script and module. Deploys a small CI/CD to AWS.

### Features
*Quarantine currently has the following features:*

- List IAM users
- Creat new IAM user/users
- Create access key (Activate & Deactivate)
- Delete access key
- Attach & detach IAM users policy/policies
- List policy/policies
- Delete IAM user/users

## Necessary packages to be install it in your enviroment

- Create a virtual env & Install 

- python3 -m pip install -U Boto3
- python3 -m pip install -U Click
- python3 -m pip install -U Botostubs
- python3 -m pip install -U Flake8

# CLI command to run your code 

- python3 covid.py --profile <use your profile name here> list-users
- python3 covid.py --profile <use your profile name here> setup-user <New user name here>
- python3 covid.py --profile <use your profile name here> list-key <user name here>
- python3 covid.py --profile <use your profile name here> deactivate-key <key here AKIAXXXXXXXXXX> <user name here>
- python3 covid.py --profile <use your profile name here> delete-key <key here AKIAXXXXXXXXXX> <user name here>
- python3 covid.py --profile <use your profile name here> setup-policy <user name here>
- python3 covid.py --profile <use your profile name here> list-policy-arn
- python3 covid.py --profile <use your profile name here> detach-policy<user name here><arn:aws::::here>
- python3 covid.py --profile <use your profile name here> delete-user<user name here>


# Help options 
- python3 covid.py --help
- import IPython; IPython.embed()
