# -*- coding:utf-8 -*-
""" Class for IAM resources """

import boto3

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



# for user in iam.list_users()['Users']:
#     print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
#     user['UserName'],
#     user['UserId'],
#     user['Arn'],
#     user['CreateDate']
#     )
#     )   