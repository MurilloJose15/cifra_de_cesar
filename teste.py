import string as st

def criptografa(texto,chave):
    letras = st.ascii_lowercase
    letras = letras.lower()
    saida = ' '
    for c in texto:
        if c in letras:
            saida+=letras[(letras.index(c) + chave) % len(letras)]
    return saida


def descriptografa(texto,chave):
    letras = st.ascii_lowercase
    letras = letras.lower()
    saida = ' '
    for c in texto:
        if c in letras:
            saida+=letras[(letras.index(c) - chave) % len(letras)]
    return saida



print(criptografa('bolsonaro', 3))
print(descriptografa('erovrqdur', 3))