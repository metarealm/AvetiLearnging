import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


def scan_QuestionAnswer(QuestionStatus, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('QuestionAnswer')
    response = table.scan(
        FilterExpression=Attr('isActive').eq(True))
    
    return response['Items']

def lambda_handler(event, context):
    # TODO implement
    try:
        query_status = True
        question = scan_QuestionAnswer(query_status)
        print(question)
        return {
            'statusCode': 200,
            'body': {"activequestion" : question}
        }
    except Exception as e: 
        print(e)
    except:
        print("Issue while activating the question")
        return {
            'statusCode': 500,
            'body': json.dumps('Issue while activating the question')
        } 

