import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''


def index(request):
        #Set files.html as a template 
        template = loader.get_template('files.html')

        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2',
                                aws_access_key_id = AWS_ACCESS_KEY_ID,
                                aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

        #use UserFiles table
        table = dynamodb.Table('UserFiles')

        #this item stores data attribute and info from UserFiles table
        items = []
        try:
                response = table.scan()

        except ClientError as e:
                print(e.response['Error']['Message'])
        else:
                context = {'items': response['Items']}
                return HttpResponse(template.render(context, request))
