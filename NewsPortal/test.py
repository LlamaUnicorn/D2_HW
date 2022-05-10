def censor(value):
    profanity = ['cunt', 'fag', 'соня', 'домик', 'дом', 'новости', 'редиска']
    print('profanity:', profanity)

    # value = 'You fag! Stupid Cunt! \nEdge case: Fag\'s voice'
    print('check text:', value)

    check_list = value.split()
    print('check_list:', check_list)
    check_list_no_sp_chars = [j.strip('.,!?:;').lower() for j in check_list]
    print('check_list_no_sp_chars:', check_list_no_sp_chars)

    i = 0

    for word in check_list_no_sp_chars:
        print('word:', word)
        if word in profanity:
            print('this is profanity')
            x = list(check_list[i])
            print('x:', x)
            censored_word = [x[0]]
            for char in x[1::]:
                if char.isalpha():
                    char = '*'
                    censored_word.append(char)
                else:
                    censored_word.append(char)
            print('censored_list', censored_word)
            result = ''.join(censored_word)
            print('result after censoring:', result)
            check_list[i] = result
        i += 1
        print('i', i)

    print('check_list:', check_list)
    value = ' '.join(check_list)
    print('final censored text:', value)
    return f'{value}'


censor("Вот он, тот самый дом, домик!")


def censor2(value):

    profanity = ['соня', 'домик', 'дом', 'новости', 'редиска']
    for i in profanity:
        if i.find(value):
            value = value.replace(i[1::], "*" * (len(i)-1))
    return f'{value}'


print(censor2('Вот он, тот самый дом, домик!'))
