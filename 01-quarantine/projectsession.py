# coding: utf-8
import botostubs
import boto3
<<<<<<< HEAD
session = boto3.Session(profile_name='PythonAuto')
iam = session.resource('iam') 


=======
session = boto3.Session(profile_name='add-your-username-here')
iam = session.client('iam') 
>>>>>>> 9ae853e7b62ebbd700d1863091163fb52dff213b


print(session.region_name)