import wordle_solver as ws


if __name__ == "__main__":
    wordle = ws.wordle_solver()
    print('update')
    # wordle.in_word_add('')
    wordle.out_of_order_letter_add('e', 3)
    wordle.out_word_add('e')
    wordle.word = ['a', None, 'p', 'l', 'e']
    wordle.out_of_order_letter_add('a', 1)
    wordle.out_of_order_letter_add('l', 1)
    wordle.out_of_order_letter_add('a', 2)
    wordle.out_of_order_letter_add('p', 0)
    wordle.out_of_order_letter_add('l', 0)
    wordle.psbl_word()
