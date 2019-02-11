# -*- coding: utf-8 -*-

'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

给定一个单词序列和一个最大宽度maxWidth，将文本进行格式化，每一行的字符长度为maxWidth。
需要使用贪婪的方法来格式化：在每一行中放入尽可能多的单词。有必要的话，可以添加额外的空格' '，来保证每行的长度严格等于maxWidth。
单词之间的空格要尽可能均分。如果一行中的空格数量不能被均分，则左边的空位要比右边的空位包含的空格数要多。
文本的最后一行，在单词之间只能出现一个空格。

备注：
一个单词指的是不包含空格的连续字符。
每个单词的长度保证大于0，且不超过maxWidth。
输入的序列至少包含一个单词。

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

'''
def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    
    """
    width = 0
    char_count = 0
    word_list = []
    for i in range(len(words)):
        # 尝试追加一个单词
        width += len(words[i])
        if i > 0:
            width += 1 # 单词之间至少加一个空格
        # 判断是否越界
        if width > maxWidth:
            break
        word_list.append(words[i])
        char_count += len(words[i])
    else: # 从来没有break过，是最后一行，也是递归结束条件
        result = ' '.join(word_list)
        result += ' ' * (maxWidth - len(result))
        return [result]
    # 将剩余空格数尽可能平均分配
    space_count = maxWidth - char_count # 需要填补的空格个数
    wc = len(word_list)
    if wc == 1: # 这一行只有一个单词，不用分配
        result = word_list[0] + ' ' * space_count
    else:
        result = word_list[0]
        basic, extra = divmod(space_count, wc - 1)
        for j in range(1, wc):
            if j <= extra: # 前extra个缝隙，要多一个空格
                result += ' '
            result += ' ' * basic + word_list[j]
    # 递归进行后面的
    return [result] + fullJustify(words[i:], maxWidth)
    
            
if '__main__' == __name__:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print('\n'.join(fullJustify(words, maxWidth)))