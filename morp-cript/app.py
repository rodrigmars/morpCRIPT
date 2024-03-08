def main():

    def text_mining(frase):

        vowels = ['a', 'e', 'i', 'o', 'u']

        punctuation = ['.', ',', ';', ':', '!',
                       '?', '...', '“', '”', '(', ')', '—']

        for p in punctuation:
            frase = frase.replace(p, '\u0020')

        def create_bag():

            words = {}

            for i, w in enumerate(frase.split()):

                # if w in vowels:
                #     continue

                words[i] = w

            def get_occurrences():

                def count_words(unique_word):

                    count = 0

                    words_dict = {}

                    for k, v in words.items():

                        if unique_word.lower() == v.lower():

                            count += 1

                            words_dict[v] = k, count

                    return words_dict

                occurrences = list(map(count_words, set(words.values())))

                result = []

                for score in occurrences:

                    for k, v in score.items():
                        result.append({"id": v[0],
                                       "word": k,
                                       "total": v[1]})

                return sorted(result,
                              key=lambda x: x["total"],
                              reverse=True)

            return get_occurrences

        return create_bag

    frase = "Cedo ou tarde.de manhã,,,você.vai aprender, assim como eu aprendi, que há uma diferença entre conhecer o caminho e percorrer o caminho"

    # frase = "areia areia areia no no olho do do do do furacão Em meio milhões"

    # frase = "c d f A A e b B i o u h t v z A f x h A"

    try:

        for occurrences in text_mining(frase)()():

            print(f"{occurrences['word']}: {occurrences['total']}")

    except Exception as ex:

        print("Error text_mining:", ex)


if __name__ == "__main__":

    main()
