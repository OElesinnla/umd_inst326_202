" A Trivia Game with sports, history and math related questions." 

class Question:
    """
    represents a game question.
    
    Attributes:
        prompt (str): The text of the question.
        answer (str): the correct answer to the question.
        category (str): the category of the question as in math, trivia, 
        sports, history.
        difficulty (str): the difficulty level of the question ('easy', 
        'medium', 'hard').
    
    """
    def __init__(self, prompt, answer, category, difficulty):
        self.prompt = prompt
        self.answer = answer
        self.category = category
        self.difficulty = difficulty
        


class MathQuestion(Question):
    """A question which requires an algebra problem to be solved.
    The question's answer will be randomly created by substituting one value
    from the prompt for a variable.
    """
    def __init__(self, prompt, category, difficulty):
        prompt, answer = self.substitute_answer_for_x(prompt)
        super().__init__(prompt, answer, category, difficulty)

    def substitute_answer_for_x(self, prompt) -> tuple[str, int]:
        """Substitute one numeric value in prompt for a variable and return the
        substituted prompt as well as the value removed.

        Args:
            prompt (str): A true equation with operators and numeric values.
        Returns:
            tuple: The prompt with a variable substituted in place of a value, 
            and that value which was substituted out.
        Raises:
            ValueError: If the prompt was not a true equation.
            NotImplementedError: If the prompt contains an unsupported operation
                (anything other than +, -, *, /, **, sqrt)
        """
        ...
    
class Game:
    """A game played with turns. Initializes with settings.

    Attributes:
        player (str): Information about the player.
        difficulty (str): The defined difficulty of the game.
        score (int): The player's score.
    """
    def __init__(self, playername):
        self.player = playername
        self.difficulty = ''
        self.score = 0

    def set_difficulty(self, option):
        """This function will let the user choose the difficulty.
        The three options are easy, medium, hard.
        Easy option will require the player to asnwer 10/20 to win
        Medium will require 15/20 to win
        Hard will require 18/20 to win"""

    def is_fail(self):
        """This method will check if the player did not achieve the goal from 
        the desired difficulty.
        If chose easy and got less than 10/20 then fail and print message
        if chose medium and got less than 15/20 then fail
        If chose hard and got less than 18/20 then fail
        will check after all questions have been answered"""
    def score(self)
        """Calculates a player's score based on how many questions the player
        gets right.
        There will be a counter that keeps track of the number of question the
        player gets right based on the data file provided by the user
        """