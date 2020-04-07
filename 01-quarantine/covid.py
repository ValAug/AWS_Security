#!/usr/bin/python
# -*- coding:utf-8 -*-

import boto3
import click
import botostubs


from usr import IAMManager

session = None
iam_manager = None


@click.group()
@click.option('--profile', default=None, help='Use a given AWS profile')

def cli(profile):
    """Covid script and module. Deploys a small CI/CD to AWS."""
    global session, iam_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)
    iam_manager = IAMManager(session)


@cli.command('list-users')
def user_list():
    """ List all IAM users """
    for user in iam_manager.all_iam()['Users']:
        print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n". format(
         user['UserName'],
         user['UserId'],
         user['Arn'],
         user['CreateDate'])
        )
    return

# create a user
@cli.command('setup-user')
@click.argument('user_name')
def setup_user(user_name):
    """Create and cofigurate a new IAM user."""
    iam_user = iam_manager.init_user(user_name)

    return


# # attach a policy
# iam.attach_user_policy(
#  UserName = 'John', 
#  PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
# )

# print(user_list())

if __name__ == '__main__':
    cli()
