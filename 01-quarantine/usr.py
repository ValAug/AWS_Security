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
        """Temporally deactivate Access Keys"""
        self.iam.update_access_key(AccessKeyId= key,
        Status='Inactive',
        UserName= user_name)

    def delete_acckeys(self, key, user_name):
        """Delete IAM user Access Keys"""
        response = self.iam.delete_access_key(AccessKeyId= key,UserName=user_name)
        print(response)

    def iam_policy(self, user_name):
        """Attache an IAM policy readable by everyone"""
        return self.iam.attach_user_policy(
            UserName = user_name,PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')


    def user_pol(self):
        """List users Policy names and ARNs"""
        for user_detail in self.iam.get_account_authorization_details()['UserDetailList']:
            policyname = []
            policyarn = []
        # find each policy attached to the user
            for policy in user_detail['AttachedManagedPolicies']:
                policyname.append(policy['PolicyName'])
                policyarn.append(policy['PolicyArn'])
        # print user details 
            print("User: {0}\nUserID: {1}\nPolicyName: {2}\nPolicyARN: {3}\n".format(
                user_detail['UserName'],
                user_detail['UserId'],
                policyname,
                policyarn)
            )
        
    def detach_policy(self, policy, user_name):
        return self.iam.detach_user_policy(UserName= user_name,PolicyArn= policy)

    def delete_user(self, user_name):
        """Delete IAM user"""
        return self.iam.delete_user(UserName= user_name)   
        
        


# paginator = my_iam_client.get_paginator('get_account_authorization_details')
# for page in paginator.paginate(Filter=['User']):
#   for user in page['UserDetailList']:
#     # Do something with user struct
