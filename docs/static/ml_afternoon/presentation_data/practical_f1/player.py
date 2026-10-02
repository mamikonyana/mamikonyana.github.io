
class Player:
    def start(self):
        """
        :return: secret, the 4-digit array that was chosen for the game.
        """
        return secret

    def guess(self):
        # TODO: construct a 4 digit array as a guess.
        pass

    def proces_oponent_reply(self, your_guess, oponent_reply):
        """
        :param your_guess: guess you have made before
        :param oponent_reply: reply that oponent has given to the previous
            guess
        """
        # TODO: Write logit to process the reply oponent has given to your
        # guess.
        pass

    def reply(self, guess):
        """
        :param guess: a 4-digit array that oponent has guessed
        :return: reply how accurate the guess is with a tuple of 2 numbers
        """
        # TODO: Given a guess reply how accurate it was.
        return reply
