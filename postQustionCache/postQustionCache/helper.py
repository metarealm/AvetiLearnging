class Question:
    def __init__(self,quesType,quesId,quesText):
        self.quesType =quesType
        self.quesText =quesText
        self.quesId =quesId
    
        
    def addAnswer(self):
        ques ={}
        if self.quesId not in ques.keys():
            ques[self.quesId]=[(self.quesId,self.quesText)]
        
    
    