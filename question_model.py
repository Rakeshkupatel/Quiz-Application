class Question:
    def __init__(self,question:str,correct_answer:str,choices:list):
        self.question_text = question #Question text
        self.correct_answer=correct_answer
        self.choices=choices