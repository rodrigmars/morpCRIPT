def main():

    def build_frase(frase):

        punctuation = ['.', ',', ';', ':', '!',
                       '?', '...', '“', '”', '(', ')', '—']

        for p in punctuation:
            frase = frase.replace(p, "\n")

        def remove_space():
            return frase.split()

        return remove_space

    words = []

    vowels = ['a', 'e', 'i', 'o', 'u']

    morpheus = "Cedo ou tarde você vai aprender, assim como eu aprendi, que há uma diferença entre conhecer o caminho e percorrer o caminho"

    for word in build_frase(morpheus)():

        if word in vowels:
            continue

        words.append(word)

    print(words)


if __name__ == "__main__":

    main()
