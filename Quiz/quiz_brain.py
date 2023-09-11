class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self, q_number):
        current_question = self.question_list[self]

#TODO this function should ask questions
#TODO Checking if the answer  was correct
#TODO checking if we're te end of the quiz