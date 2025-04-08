

class Question:
    """
    represents a game question.
    
    Attributes:
        prompt (str): The text of the question.
        answer (str): the correct answer to the question.
        category (str): the category of the question as in math, trivia, sports, history.
        difficulty (str): the difficulty level of the question ('easy', 'medium', 'hard').
    
    """
    def __init__(self, prompt, answer, category, difficulty):
        self.prompt = prompt
        self.answer = answer
        self.category = category
        self.difficulty = difficulty