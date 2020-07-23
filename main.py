
import sys
import boto3
import mysql.connector
import redis

ENDPOINT="aeveti.cqpjkxoacehw.us-west-1.rds.amazonaws.com"
PORT="3306"
USR="admin"
REGION="us-east-1"


mydb = mysql.connector.connect(
  host="avetiqna.dmtu9m.ng.0001.usw2.cache.amazonaws.com",
  user="admin",
  password="admin123",
  database="Aveti"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
  
r = redis.Redis(
    host='aveti.buqzry.ng.0001.usw1.cache.amazonaws.com',
    port=6379)
  
r.set('Q001', '<div id="video_question_div" style="margin-top: 5px; height: 85%;">\
		    <div id="video_question_text_div" style="margin-top: 5px; margin-bottom: 10px;">\
                       <p style="font-size:19px;">   \
			what is the capital of india\
                       </p>\
		    </div>\
                    <hr/>\
		    <div id="video_question_radio" style="margin-top: 10px; margin-left: 50px;font-size:18px;"><input type="radio" name="answer_option" value="7" style="margin-bottom:15px;margin-right:3px;">nd</input><br /><input type="radio" name="answer_option" value="8" style="margin-bottom:15px;margin-right:3px;">paris</input><br /></div>\
		</div>\
		<div id="video_question_div" style="height: 85%; margin-top: 5px;">\
		    <div id="video_question_text_div" style="margin-top: 5px; margin-bottom: 10px;">\
                     <p style="font-size:19px;"> \
			what is capitralk opf india\
                     </p>\
		    </div>\
                     <hr/>\
		    <div id="fb_answer_div" style="margin-top: 10px; margin-bottom: 5px; margin-left: 50px;">\
			Your Answer : <input typ="text" name="fb_correct_answer" id="fb_correct_answer" /> \
		    </div>\
		</div>')
print("Value of Q001" ,r.get('Q001'))

print("hello sql")