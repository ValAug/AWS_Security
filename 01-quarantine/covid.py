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

# Create a user
@cli.command('setup-user')
@click.argument('user_name')
def setup_user(user_name,):
    """Create and cofigurate a new IAM user."""
    iam_user = iam_manager.init_user(user_name)


# Create a new set of key
@cli.command('setup-key')
@click.argument('user_name')
def access_key(user_name):
   """Create new Access Keys"""
   iam_user = iam_manager.new_keys(user_name)

# List user Access Key
@cli.command('list-key')
@click.argument('user_name')
def access_key(user_name):
   """List all Access Keys"""
   iam_user = iam_manager.list_acckeys(user_name)

# Update keys status
@cli.command('deactivate-key')
@click.argument('key')
@click.argument('user_name')
def update_keys(key, user_name):
    """Deactivate IAM user keys"""
    iam_user = iam_manager.deactivate_keys(key, user_name)

# Delete user keys 
@cli.command('delete-key')
@click.argument('key')
@click.argument('user_name')
def update_keys(key, user_name):
    """Deactivate IAM user keys"""
    iam_user = iam_manager.delete_acckeys(key, user_name)

# Attach a policy to an active user
@cli.command('setup-policy')
@click.argument('user_name')
def setup_user(user_name):
    """Create and cofigurate a new IAM user."""
    iam_user = iam_manager.iam_policy(user_name)

# List all users Polocies and ARNs
@cli.command('list-policy-arn')
def pol_arn():
    """List all users Policies and ARNs details"""
    iam_user = iam_manager.user_detail()
    return




# print(user_list())

if __name__ == '__main__':
    cli()
