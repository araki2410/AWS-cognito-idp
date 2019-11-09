from aws_srp import AWSSRP

user_name = "youryouryourname@gmail.com"
passwd = "passPassPassword"
region = "ap-northeast-1" #your region
user_poolId = "ap-northeast-1_123yyyXXX"
clientId = ""

aws = AWSSRP(username=user_name, password=passwd, pool_id=user_poolId,
             client_id=clientId, pool_region=region)

tokens = aws.authenticate_user()
id_token = tokens['AuthenticationResult']['IdToken']
refresh_token = tokens['AuthenticationResult']['RefreshToken']
access_token = tokens['AuthenticationResult']['AccessToken']
token_type = tokens['AuthenticationResult']['TokenType']

print("id_token:\n", id_token, "\n")
print("refresh_token:\n", refresh_token, "\n")
print("access_token:\n", access_token, "\n")
