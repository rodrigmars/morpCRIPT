def main():

    def pick_up_words(frase):

        vowels = ['a', 'e', 'i', 'o', 'u']

        punctuation = ['.', ',', ';', ':', '!',
                       '?', '...', '“', '”', '(', ')', '—']

        for p in punctuation:
            frase = frase.replace(p, '\u0020')

        def create_bag():

            words = []

            for w in frase.split():

                # if w in vowels:
                #     continue

                words.append(w)

            def Counter():

                def count_words(unique_word):

                    words_dict = {}
                    count = 0

                    for w in words:

                        if unique_word.lower() == w.lower():

                            count += 1
                            words_dict[unique_word] = count

                    return words_dict

                return list(map(count_words, set(words)))

            return Counter

        return create_bag

    # frase = "Cedo ou tarde.de manhã,,,você.vai aprender, assim como eu aprendi, que há uma diferença entre conhecer o caminho e percorrer o caminho"
    frase = "areia areia areia no no olho do do do do furacão Em meio milhões"

    words = pick_up_words(frase)()()

    for w in words:
        print(w)


if __name__ == "__main__":

    main()
