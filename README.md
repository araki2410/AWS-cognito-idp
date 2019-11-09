# AWS cognito-idp: Get client Tokens

## Require info
```
user_name  : client_cog-idp@hogemail.com
password   : mypassword-hogehoge
client_ID  : 0123456789abcdef0123456789
userpool_ID: ap-northeast-1_aBCDEFG89
```

- client_ID consist of 26 chars
- userpool_ID consist of <region>_<unique_service_ID>
- <region> is ap-northeast-1 in japan. [AWS: Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- <unique_service_ID> is consist of 9 chars

### I want to know userpool_ID and/or client_ID !

- I'm an AWS user: Look AWS Web page
- I'm a not AWS user (mean I'm a user of services using AWS): Have you an account? Let's capture the packet!

----
#### Capture the packet

Use some capturing tool. e.g) Wireshark, Burp Suite or etc.  
And login tha service.

target: https;/cognito-idp.<region>.amazon.com  

client_ID is in there.   
userpool_ID is ecrypted.

Decode the value by base64 in any reply:
```
{"AuthenticationResult":
{"AccessToken":"4LTYhFhn....SJIg",
"ExpiresIn":3600,
"IdToken":"ZWF.E1Fb....KCB",
"RefreshToken":"sEMh.N....6Hp3mhze"
```
