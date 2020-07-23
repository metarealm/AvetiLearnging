import sys
import os
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import pymysql
import redis
import constants as cnst

def setQuestionHTML(question):
    questionhtml = cnst.QUESTION_STRING.replace("{{question_string}}", question)
    return questionhtml
    
def setAnswerHTML(answers):
    if(len(answers) == 0 ) :
        answershtml = cnst.INPUT_ANSWER_STRING
    else:
        answerhtmls = []
        for answer in answers:
            answerhtmls.append(cnst.RADIO_BUTTON_EACH_ANSWER_STRING.replace("{{answer}}", answer))
        answershtml = cnst.RADIO_BUTTON_ANSWER_STRING.replace("{{answerhtmls}}", "<BR>".join(answerhtmls))
    return answershtml
    
def setQnAHTML(questionHTML , answerHTML):
    qnaHTML = cnst.QUESTION_ANSWER_STRING.replace("{{question_section}}",questionHTML).replace("{{asnwer_section}}",answerHTML)
    return qnaHTML

def pushToRedis(questionID ,questionhtml):
    r = redis.Redis(
        host=cnst.RADIS_HOST,
        port=6379)
      
    r.set(questionID, questionhtml)
    print("Value of Q001" ,r.get(questionID))


def getDBData():
    conn = pymysql.connect(
        host="aeveti.cqpjkxoacehw.us-west-1.rds.amazonaws.com", 
        port=3306, 
        user="admin", 
        passwd="admin123", 
        db="Aveti",
        connect_timeout=3)
    
    print(conn)
    
        
    cur = conn.cursor()
    sub="Hist"
    chapter ="chap1"
    query ="SELECT * FROM ors_live_class_question where course_id =\"%s\" and chap_id = \"%s\"" %(sub,chapter)
    print(query)
    cur.execute(query )
    results =cur.fetchall()
    #print(results)
    ans_val =[]
    ans_optionSeq =[]
    dic1={}
    
    for row in results:
        ques_text=row[4]
        question_id =row[0]
        if question_id not in dic1.keys():
            dic1[question_id]=[(question_id,ques_text)]
        #print("ques :",ques_text)
        #print("ques_id",question_id)
        #print("option type",row[3])
        if row[3]=="radio":
            
            ans_val.append(row[5])
            ans_optionSeq.append(row[6])
        else:
            ans_val.append(row[5])
            ans_optionSeq.append("True")
        dic1[question_id].append((row[6],row[5]))
        #print("ques :",ques_text)
        #print("ques_id",question_id)
    answer_option =zip (ans_optionSeq,ans_val)        
            
        
    cur.execute("SHOW TABLES")
    cur.execute("SHOW TABLES")
    
    return dic1

def lambda_handler(event, context):
    # TODO implement
    ques_detail ={}
    ques_detail = getDBData()
    for key in ques_detail:
        print(ques_detail[key])
        
    #print("qustion is ",ques_id)
    #print("question",question)
    #print("answer",answers)
    
    #questionhtml = setQuestionHTML(question)
    #answerhtml = setAnswerHTML(answers)
   # qnaHTML = setQnAHTML(questionhtml ,answerhtml)
    #pushToRedis("Q001" ,qnaHTML)
   # return {
    #    "statusCode": 200,
    #    "headers": {
    #        "x-custom-header" : "my custom header value"
    #    },
    #    "body": questionhtml
    #}