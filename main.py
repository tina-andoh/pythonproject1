# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import TextIO


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# a = 0
# for x in range(100, 200):
#     if x % 2 != 0:
#         a += x
# print(a)
####################################################################################################################################3
###working with files (how to extract even numbered lines from a file)
# f = open('input.txt', 'w')
# f.write("Twas brillig, and the slithy toves\nSome things in life are bad, they can really make you mad\nDid gyre and gimble in the wabe:\nOther things just make you swear and curse\nAll mimsy were the borogoves,\nWhen you're chewing on life's gristle, don't grumble give a whistle\nAnd the mome raths outgrabe.\nThis will help things turn out for the best\n'Beware the Jabberwock, my son!\nAlways look on the bright side of life\nThe jaws that bite, the claws that catch!\nAlways look on the right side of life\nBeware the Jubjub bird, and shun\nIf life seems jolly rotten, there's something you've forgotten\nThe frumious Bandersnatch!'\nAnd that's to laugh and smile and dance and sing\nHe took his vorpal sword in hand:\nWhen you're feeling in the dumps, don't be silly, chumps\nLong time the manxome foe he sought --\nJust purse your lips and whistle, that's the thing\nSo rested he by the Tumtum tree,\nSo, always look on the bright side of death\nAnd stood awhile in thought.\nJust before you draw your terminal breath\nAnd, as in uffish thought he stood,\nLife's a counterfeit and when you look at it\nThe Jabberwock, with eyes of flame,\nLife's a laugh and death's the joke, it's true\nCame whiffling through the tulgey wood,\nYou see, it's all a show, keep them laughing as you go\nAnd burbled as it came!\nJust remember the last laugh is on you\nOne, two! One, two! And through and through\nAlways look on the bright side of life\nThe vorpal blade went snicker-snack!\nAnd always look on the right side of life\nHe left it dead, and with its head\nAlways look on the bright side of life\nHe went galumphing back.\nAnd always look on the right side of life")
# # inputfile = ['Bravely bold Sir Robin rode forth from Camelot', 'Yes,brave Sir Robin turned about', 'He was not afraid to die, O brave Sir Robin',
#              'And gallantly he chickened out', 'He was not at all afraid to be killed in nasty ways',
#              'Bravely talking to his feet', 'Brave, brave, brave, brave Sir Robin', 'He beat a very brave retreat']
# for i in inputfile:
#     f.write(str(i)+'\n')
# a = 1
# f = open('input.txt','r')
# for line in f.readlines():
#     if a % 2 == 0:
#         print(line)
#     a += 1
###another method to do it but the output will be in a file format
# f = open('file.txt', 'w')
# f.write('Bravely bold Sir Robin rode forth from Camelot\nYes,brave Sir Robin turned about\nHe was not afraid to die\nO brave Sir Robin\nAnd gallantly he chickened out\nHe was not at all afraid to be killed in nasty ways\nBravely talking to his feet\nBrave, brave, brave, brave Sir Robin\nHe beat a very brave retreat')
# f = open('file.txt','r')
# fn1 = open('output.txt','w')
# cont = f.readlines()
# print(cont)
# # type(cont)
# i = 1
# for line in cont:
#     if i % 2 == 0:
#         a = str(cont[i])
#         print(a)
#         fn1.write(a)
#     i += 1
#     # else:
#     #     pass
#
# fn1.close()

# i = 1
# f = open('file.txt','r')
# for line in f.readlines():
#     if i % 2 == 0 :
#         print(line)
    #i += 1
#################################################################
##working with dictionaries
#s = ["We", "tried", "list", "and","we", "tried", "dicts", "also", "we", "tried", "Zen"]
# s = ("We tried list and we tried dicts also we tried Zen")
# a = s.split(' ')
# print(a)
# # for words in s.split(' '):
# #     a = words
# #     print(a)
# dict = {}
# for words in a:
#     if words in dict:
#         dict[words] = dict[words]+1
#     else:
#         dict[words] = 1
# # print(dict)
# for key, value in dict.items():
#     print(key, value)
#     # print(value)

# s = ("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be")
# a = s.split(' ')
# print(a)
# for words in s.split(' '):
#     a = words
#     print(a)
# dict = {}
# for words in a:
#     if words in dict:
#         dict[words] = dict[words]+1
#     else:
#         dict[words] = 1
# # print(dict)
# for key, value in dict.items():
#     print(key, value)
    # print(value)

# dict = {'We':3, 'tried':3, 'list':1, 'and':1, 'dicts':1, 'also':1, 'Zen':1}
# for key, value in dict.items():
#     print(key, value)
#     # print(value)

#############################################################
##counting the number of bases in a string of bases
# a = ("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
# b = [a.count("A"), a.count("C"), a.count("G"), a.count("T")]
# ##The code below outputs the integers to be seperated by space and not in a list form as it sbould be
# print(*b, sep=" ")

seq = ("GACATCCCACTGAAACAGTAGGGAGTCGAGGGTCCCGTATCCATCTTCTGAATGCAGCATAATTGGTCTGTAAGGATGCCCAACCACACCGTAGCACGGATTTGGAAGACGTGTCAGAACCTGGTTTACCGCTCCGGGATCTGGTACATTCTCTCTTGGCGGGCACCAGGGTAGATACATCGAGTCTTTAACCTATAAGCAGTGCTTCGCACTACTCGTTTTTACAGACGACAGCCCGAACACAGGCGGCTTGTCAGCACGAATTCATAATTGGTTCAATTCTCAGCCAACCGAGGTTGGAAACAGTTGGGGCTTCTAGTACGTGGTGCTCTGTTAACTGTGTTAGCATGAAGTCTAGGACAAGGCGGCGTGAGATTGCGCGGGCAGCCATGATCAAGAAGCCCCCATCTCTAACGGCCACGGTATACCTGGTAACAGAATCAGGAAGCAATGGAATAAATACTAGTTCTCTTCATTGTTCTCTTACGCTGAATACATTTTATGCTGGGAAAAGTTCGCTCCCTTTCACTTTGAATCAAGTACGGTGACGCAGACCACTGTTCTCTGGCATTTTGGAGTAAAGATCACGTGCGCGTTACTACCTTTTCTACAAAGAATGAGTCACGGTTCGGATTATCCGATAAGTACAACGTTAGAGTGTATTAGACATATTCTGATAACGTAATGAGAGTGGACACACACAATTTTCGCTGCCACGGCACTTAGAGCTTTGGTGTAATCCAACGTAAAGGCCCTTTAGTTTTTTAGCAAGTTAGCGTCACTACCTCATACCTCAGTTCGTCACCAACCTGGACCCGTAGACTAAGAAGGAAGACGTGGGGAGGTTCAATGGTAAGATATAAAATGTGCAGTAGCCTATAACGAGGTAATCCGAGATAGTGTTATCGCGCTCTTTGATTAGTCCGACGGTACCTTGAT")
seq_count = [seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")]
print(*seq_count, sep=" ")