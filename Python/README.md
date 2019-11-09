## Python
- python3
- python2.7 or more over

## Require pip module
```
$ pip3 install boto3
```

### aws configure
- install awscli , or
- overwrite boto3

[Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html)
```
$ pip3 install awscli --upgrade --user
$ aws configure
<type some bullshit>

$ ls ~/.aws/
config   credentials
```

#### Overwrite the boto3/session.py
```
class Session(object):
    #def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
    def __init__(self, aws_access_key_id="hogehoge", aws_secret_access_key="piyopiyo",
                 aws_session_token=None, region_name=None,
                 botocore_session=None, profile_name=None):
```

----
### Refference
- [warrant](https://github.com/capless/warrant)