def response(hey_bob):
    respuesta = hey_bob.strip()
    if (respuesta.endswith("?") and not respuesta.isupper()): return "Sure."
    if respuesta.isupper() and not respuesta.endswith("?") : return "Whoa, chill out!"
    if (respuesta.isupper() and '?' in respuesta): return "Calm down, I know what I'm doing!"
    if not respuesta: return "Fine. Be that way!"
    return "Whatever."
     
    pass
