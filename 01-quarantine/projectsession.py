# coding: utf-8
import botostubs
import boto3

session = boto3.Session(profile_name='profile_name_here')
iam = session.resource('iam') 




print(session.region_name)