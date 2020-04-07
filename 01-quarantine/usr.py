# -*- coding:utf-8 -*-
""" Class for IAM resources """

import boto3
import botostubs
from botocore.exceptions import ClientError

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
        """Create new IAM user, or Return existing one by name """
        iam_user = None

        try:

            iam_user = self.iam.create_user(UserName=user_name)
        
        except ClientError as error:
            if error.response["Error"]["Code"] == "IAM user already exist":
                iam_user = self.iam.create_user(user_name)
        
        return iam_user

