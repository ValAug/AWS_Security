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
        self.iam = self.session.client('iam') # type: botostubs.IAM
    

        self.manifest = {}

    def all_iam(self):
        """Get IAM users list """
        return self.iam.list_users()

    def init_user(self, user_name, access_key):
        """Create new IAM user(Entity), or Return an Entity Already Exists"""

        iam_user = None
        active_user = None
        
        try:

            return self.iam.create_user(UserName=user_name)

        except ClientError as error:
            print(error)
            raise click.Abort()
        
        return iam_user

    # Create an access key
    def new_keys(self, user_name):
        """Create new Access Keys"""
        try:
            response = self.iam.create_access_key(
             UserName = user_name) 
            AccessKey = response['AccessKey']['AccessKeyId']
            SecretAccessKey = response['AccessKey']['SecretAccessKey']
            return AccessKey, SecretAccessKey

        except ClientError as error:
            print(error)
            raise click.Abort()

    def list_acckeys(self, user_name):
        """List IAM user Access Keys"""
        response = self.iam.list_access_keys(UserName=user_name)
        print(response)
        
    def deactivate_keys(self, key, user_name):
        self.iam.update_access_key(AccessKeyId= key,
        Status='Inactive',
        UserName= user_name)

    def delete_acckeys(self, key, user_name):
        """Delete IAM user Access Keys"""
        response = self.iam.delete_access_key(AccessKeyId= key,UserName=user_name)
        print(response)

    def iam_policy(self, user_name):
        """Set an IAM policy to be readable by everyone"""
        return self.iam.attach_user_policy(
            UserName = user_name,PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')

        return

    def user_detail(self):
        """List users Policy names and ARNs"""
        for user_detail in self.iam.get_account_authorization_details(Filter=['User'])['UserDetailList']:policyname = [] 
        policyarn = []
        
        print(user_detail, '\n')

        # except ClientError as error:
        #     if error.response["Error"]["Code"] == "EntityAlreadyExists":
        #         iam_user = self.iam.get_user(UserName=user_name)
        #     else:
        #         raise
        
        

