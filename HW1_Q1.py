def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    length_word = len(word)

    if length_word<6:
        return False

    if length_word > 6:
        flag = 0
        for i in range(1, (length_word - 4)):
            if word[i - 1] == word[i]:
                if word[i + 1] == word[i + 2]:
                    if word[i + 3] == word[i + 4]:
                        flag = 1
                        return True

            if i == (length_word - 5):
                if flag == 0:
                    return False

    if length_word == 6:
        i=1
        if word[i-1] == word[i]:
              if word[i + 1] == word[i + 2]:
                 if word[i + 3] == word[i + 4]:
                   flag = 1
                   return True
                 else:
                     return False
              else:
                  return False
        else:
               return False