# -*- coding:utf-8 -*-
""" Class for IAM resources """

import boto3
import botostubs
from botocore.exceptions import ClientError
import click


# iam = boto3.client('iam')

class IAMManager:
    """ Manage IAM user """

    def __init__(self, session):
        self.session = session
        self.iam = self.session.client('iam')

        self.manifest = {}

    def all_iam(self):
        """Get IAM users list """
        return self.iam.list_users()

    def init_user(self, user_name):
        """Create new IAM user(Entity), or Return an Entity Already Exists"""

        iam_user = None
        active_user = None
        

        try:

            return self.iam.create_user(UserName=user_name)
            # iam_user = self.iam.create_user(UserName=user_name)
        
        except ClientError as error:
            print(error)
            raise click.Abort()
        
        return iam_user

    def iam_policy(self, user_name):
        """Set IAM policy to be readable by everyone"""
        return self.iam.attach_user_policy(
            UserName = user_name,PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')

        return

        # except ClientError as error:
        #     if error.response["Error"]["Code"] == "EntityAlreadyExists":
        #         iam_user = self.iam.get_user(UserName=user_name)
        #     else:
        #         raise
        
        

