from pymorphy3 import MorphAnalyzer
morph = MorphAnalyzer(lang='ru')


def process_input(full_inp, pos):
    inp_s = full_inp.split('.')
    if len(inp_s) == 2:
        inp = inp_s[0]  # лемма/словоформа
        inp_pos = [inp_s[1]]  # тег
    elif len(inp_s) == 1:
        inp = inp_s[0]  # тег/лемма/словоформа
        inp_pos = pos
    else:
        return 0

    return inp, inp_pos


def get_lemma(inp, inp_pos, translate):
    if len(inp_pos) == 1:
        inp_morph = morph.parse(inp)
        i = 0
        try:
            while inp_pos[0] not in translate[inp_morph[i].tag.POS]:
                i += 1
            inp_lemms = inp_morph[i].normal_form
        except:
            return 0

    else:
        inp_morph = morph.parse(inp)[0]  # если часть речи не указана, берем самый вероятный разбор
        inp_lemms = inp_morph.normal_form

    return inp_lemms

