import traceback
# import logging


def main():

    def text_mining(frase):

        punctuation = ['.', ',', ';', ':', '!',
                       '?', '...', '“', '”', '(', ')', '—']

        for p in punctuation:
            frase = frase.replace(p, '\u0020')

        def get_occurrences():

            occurrences = list(map(lambda x: {"word": x, "total": frase.split().count(x)},
                                   set(frase.split())))

            return sorted(occurrences, key=lambda x: x["total"], reverse=True)

        return get_occurrences

    # frase = "Cedo ou tarde.de manhã,,,você.vai aprender, assim como eu aprendi, que há uma diferença entre conhecer o caminho e percorrer o caminho"

    # frase = "areia areia areia no no olho do do do do furacão Em meio milhões"

    frase = "porta quadro mesa janela mesa poltrona janela casa cadeira mesa sofá porta janela parede mesa sofá quadro"

    # frase = "c d f A A e b B i o u h t v z A f x h A"

    try:

        for occurrences in text_mining(frase)():

            print(f"{occurrences['word']}: {occurrences['total']}")

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":

    main()
