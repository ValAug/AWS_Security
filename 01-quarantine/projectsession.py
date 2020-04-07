# coding: utf-8
import botostubs
import boto3

session = boto3.Session(profile_name='PythonAuto')
iam = session.resource('iam') 




print(session.region_name)