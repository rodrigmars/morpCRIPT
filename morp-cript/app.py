import traceback
# import logging


def main():

    def text_mining(frase):

        # vowels = ['a', 'e', 'i', 'o', 'u']

        punctuation = ['.', ',', ';', ':', '!',
                       '?', '...', '“', '”', '(', ')', '—']

        for p in punctuation:
            frase = frase.replace(p, '\u0020')

        words = frase.split()

        def get_occurrences():

            def count_words(unique_word):

                count = 0

                words_dict = {}

                for w in words:

                    if unique_word.lower() == w.lower():

                        count += 1

                        words_dict[w] = count

                return words_dict

            occurrences = list(map(count_words, set(words)))

            word_dictionary = []

            for score in occurrences:

                for k, v in score.items():
                    word_dictionary.append({"word": k,
                                            "total": v})

            return sorted(word_dictionary,
                          key=lambda x: x["total"],
                          reverse=True)

        return get_occurrences

    # frase = "Cedo ou tarde.de manhã,,,você.vai aprender, assim como eu aprendi, que há uma diferença entre conhecer o caminho e percorrer o caminho"

    frase = "areia areia areia no no olho do do do do furacão Em meio milhões"

    # frase = "c d f A A e b B i o u h t v z A f x h A"

    try:

        for occurrences in text_mining(frase)():

            print(f"{occurrences['word']}: {occurrences['total']}")

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":

    main()
