# -*- coding: utf-8 -*-

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

给定两个词（起始词和结束词），和一个词数组，找到从起始词到结束词的转移序列的最短长度。
每次转移只能改变一个字符。
每个转移词职能从词数组中挑选。
起始词不算到转移词中。
备注：
如果没有转移序列，则返回0。
所有单词有相同的长度。
所有单词只包含小写字母。
词序列中无重复元素。
起始词和结束词非空，且不同。

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import string
def ladderLength(beginWord: str, endWord: str, wordList: list) -> int:
    """
    维护两个单词集合前向集和后向集，每次递归时选择其中一个较小集合，构造其下一层集合。直至两个集合对接成功。
    """
    if endWord not in wordList:
        return 0
    def build_next_level(set1, set2, word_set, result):
        """
        从word_set中筛选set1的所有子节点，构成新的set1，同时路径长度+1。
        然后继续递归下一层。
        result[0]: 存放最短长度
        """
        # 挑选较小集合
        if len(set1) > len(set2):
            build_next_level(set2, set1, word_set, result)
            return
        # 递归结束条件
        if not set1:
            result[0] = 0
            return
        # 寻找set1的下一层
        new_set1 = set()
        for word in set1:
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in set2: # 触达到了set2，递归结束
                        result[0] += 1
                        return
                    if new_word in word_set: # 新词在候选集中
                        new_set1.add(new_word)
        # 缩减候选集
        for word in new_set1:
            word_set.discard(word)
        result[0] += 1
        build_next_level(new_set1, set2, word_set, result)
    
    result = [1]
    build_next_level({beginWord}, {endWord}, set(wordList) - {endWord}, result)
    return result[0]

def ladderLength2(beginWord: str, endWord: str, wordList: list) -> int:
    """
    对第一种方法的优化。
    寻找set1的下一层节点时，不再每个字符都遍历一遍a-z，而是从提前根据wordList构建好的字典<'a_b':{'acb','adb'}>中取值。
    不过不会减少复杂度，因为就算遍历一遍a-z也是固定的26个字母，是常量，不影响复杂度。
    """
    if endWord not in wordList:
        return 0
    def build_next_level(set1, set2, word_set, word_dict, result):
        """
        从word_dict中筛选set1的所有子节点，构成新的set1，同时路径长度+1。
        然后继续递归下一层。
        result[0]: 存放最短长度
        """
        # 挑选较小集合
        if len(set1) > len(set2):
            build_next_level(set2, set1, word_set, word_dict, result)
            return
        # 递归结束条件
        if not set1:
            result[0] = 0
            return
        # 寻找set1的下一层
        new_set1 = set()
        for word in set1:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i+1:]
                for new_word in word_dict.get(key, set()):
                    if new_word in set2: # 触达到了set2，递归结束
                        result[0] += 1
                        return
                    if new_word in word_set: # 新词在候选集中
                        new_set1.add(new_word)
        # 缩减候选集
        for word in new_set1:
            word_set.discard(word)
        result[0] += 1
        build_next_level(new_set1, set2, word_set, word_dict, result)
    
    # 构造字典
    word_dict = dict()
    for word in wordList:
        if word == endWord:
            continue
        for i in range(len(word)):
            key = word[:i] + '_' + word[i+1:]
            word_dict[key] = word_dict.get(key, set()) | {word} 
    result = [1]
    build_next_level({beginWord}, {endWord}, set(wordList) - {endWord}, word_dict, result)
    return result[0]

if '__main__' == __name__:
    beginWord = "cet"
    endWord = "ism"
    wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    print(ladderLength2(beginWord, endWord, wordList))
