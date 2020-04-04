# coding: utf-8

import boto3
session = boto3.Session(profile_name='add-your-username-here')
iam = session.client('iam') 


print(session.region_name)
