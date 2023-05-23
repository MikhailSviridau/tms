words = input()
word_list = words.split()
word_1, word_2 = word_list[0], word_list[-1]
print(f"""!{word_2}! ! !{word_1}!""")
print('!{var}! ! !{var}!'.format(var=word_1, var1=word_2))