import re
import traceback
# import logging


def main():

    def text_mining(frase: str):

        words = re.sub(r'[^\w\s]', '\u0020', frase).split()

        def get_occurrences():

            occurrences = {word: words.count(word)
                           for word in set(words)}

            return sorted(occurrences.items(), key=lambda w: w[1], reverse=True)

        return get_occurrences

    # frase = "Cedo ou tarde.de manhã,,,você.vai aprender, assim como eu aprendi, que há uma diferença entre conhecer o caminho e percorrer o caminho"

    frase = "\\porta.quadro?mesa!janela/mesa poltrona janela casa cadeira mesa sofá porta janela parede mesa sofá quadro"

    # frase = "c d f A A e b B i o u h t v z A f x h A"

    try:

        for words in text_mining(frase)():

            print(words)

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":

    main()
