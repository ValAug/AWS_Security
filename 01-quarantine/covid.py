#!/usr/bin/python
# -*- coding:utf-8 -*-

import boto3
import click

#iam = boto3.client('iam')

from usr import IAMManager

session = None
iam_manager = None

@click.group()
@click.option('--profile', default=None, help='Use a given AWS profile.')

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
        print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
        user['UserName'],
        user['UserId'],
        user['Arn'],
        user['CreateDate']
        )
        )   
    return

# print(user_list())

if __name__ == '__main__':
    cli()