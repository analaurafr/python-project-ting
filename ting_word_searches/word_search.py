def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        metadata = instance.search(i)
        occurrences = []

        for index, line in enumerate(metadata["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": metadata["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        metadata = instance.search(i)
        occurrences = []

        for index, line in enumerate(metadata["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": metadata["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result
