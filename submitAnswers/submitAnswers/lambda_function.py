import redis
import json

def submitAnswer(question_Id, option, student_name, dynamodb=None):
    key = question_Id+"_"+option
    print(key)
    redisClient = redis.StrictRedis(host='aveit-qna-001.spyhdd.0001.usw2.cache.amazonaws.com', port=6379, db=0)
    redisClient.rpush(key, student_name)
    # Print the contents of the Redis list
    # while(redisClient.llen(key)!=0):
    print(key + " has enties " + str(redisClient.llen(key)))
    
def lambda_handler(event, context):   
    try:
        questionID = event["questionID"]
        answer = event["answer"]
        userID = event["userID"]
        submitAnswer(questionID, answer, userID)
        return {
            'statusCode': 200,
            'body': json.dumps('Submitting answer was successful')
        }
    except Exception as e: 
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('error while submitting answer')
        }
    except:
        print("error while submitting answer")
        return {
            'statusCode': 500,
            'body': json.dumps('error while submitting answer')
        }
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }