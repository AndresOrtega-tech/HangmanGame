class HangmanGame:

    secret_words = {
        'facil': 'gato',
        'intermedio': 'carnaval',
        'avanzado': 'cronométrico',
    }

    def __init__(self):
        self.word = None
        self.guesses = set()
        self.game_is_on = True
        self.word_status = None

    def play(self):
        print("======== Bienvenido al juego del ahorcado ========")
        print("Selecciona 0 para terminar el juego.")
        print("Elige el nivel de dificultad:")
        print(*self.secret_words.keys(), sep=' - ')
        level = input()
        while True:
            if level == '0':
                game.game_is_on = False
                break
            elif level in self.secret_words:
                break
            else:
                print('Debes ingresar un nivel válido')
                level = input()
        self.word = self.secret_words[level]
        self.word_status = '_' * len(self.word)
        while self.game_is_on:
            self.guess()
        replay = input('¿Quieres jugar de nuevo? (s/n): ')
        if replay == 's':
            self.reset()
            self.play()
        elif replay == 'n':
            print('Gracias por jugar')

    def guess(self):
        print('Adivina una letra')
        letter = input()
        if letter == '0':
            self.game_is_on = False
        elif letter.isalpha() and len(letter) == 1:
            self.guesses.add(letter)
            self.update_word_status()
        else:
            print('Debes ingresar solo una letra')

    def update_word_status(self):
        current_word_status = ''
        for character in self.word:
            if character in self.guesses:
                current_word_status += character
            else:
                current_word_status += '_'
        self.word_status = current_word_status
        if self.word_status == self.word:
            print('¡Felicidades, ganaste!')
            self.game_is_on = False
            print(f"La palabra era: {self.word}")
        else:
            print(self.word_status)

    def reset(self):
        self.word = None
        self.guesses = set()
        self.game_is_on = True
        self.word_status = None


if __name__ == '__main__':
    game = HangmanGame()
    game.play()