import wordle_solver as ws

if __name__ == "__main__":
    wordle = ws.wordle_solver()
    print('update')
    wordle.in_word_add('')
    wordle.out_word_add('')
    wordle.word = [None, None, None, None, None]
    print('psbl_word')
    wordle.psbl_word()
