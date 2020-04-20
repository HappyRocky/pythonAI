# -*- coding: utf-8 -*-

"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

给定两个词（起始词和结束词），和一个词数组，找到最短的转移序列，从起始词到结束词。
每次转移只能改变一个字符。
每个转移词职能从词数组中挑选。
起始词不算到转移词中。
备注：
如果没有转移序列，则返回空序列。
所有单词有相同的长度。
所有单词只包含小写字母。
词序列中无重复元素。
起始词和结束词非空，且不同。

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

def findLadders(beginWord: str, endWord: str, wordList: list) -> list:
    """
    深度优先遍历 + 贪婪
    从起始词开始，将词序列中按照与结束词的相似度排序，然后依次作为转移词，继续循环。
    时间复杂度为 O(ln^2)，其中 l 为单词长度，n 为词序列长度。
    """
    if endWord not in wordList:
        return []
    def get_diff_idx(str1, str2):
        """
        返回两个字符串的字符不同的位置
        """
        result = []
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                result.append(i)
        return result
    def find_ladders(cur_result: list, except_set: set, endWord, wordList, result_list: list):
        """
        递归，以当前转移词序列为基础，继续挑选转移词，直至结束词。
        cur_result:当前转移词序列
        except_set:需要从wordList中排除的词，不作为候选转移词
        endWord:结束词
        wordList:词序列
        result_list:最终结果数组
        """
        # 递归结束条件
        if cur_result[-1] == endWord: # 到达终点
            if not result_list or len(result_list[0]) == len(cur_result):
                result_list.append(cur_result)
            elif len(result_list[0]) > len(cur_result):
                result_list.clear()
                result_list.append(cur_result)
            return
        elif result_list and len(result_list[0]) <= len(cur_result): # 没到达终点，但是长度已经达到了历史最短路径
            return
        # 从词序列中挑选与当前词只差一个字符的词，并按照相似度排序
        next_list = []
        cur_word = cur_result[-1]
        
        # 遍历词列表，判断哪个词与当前词只差1个字符，复杂度为O(nl) ################
        for word in wordList:
            if word not in except_set:
                diff_idxs = get_diff_idx(word, cur_word) # 相差几个字符
                if len(diff_idxs) == 1: # 只差一个字符，则加入下一个转移词的候选名单
                    if endWord[diff_idxs[0]] == word[diff_idxs[0]]: # 改变字符之后，更接近结束词
                        next_list.insert(0, word) # 优先级高
                    else:
                        next_list.append(word) # 优先级低
        
        if not next_list: # 无候选词，这条路不通
            return
        # 递归继续寻找下一个
        except_set_new = except_set | set(next_list) # 候选名单的所有词之后都不必再考虑，否则当前考虑就可以
        for word in next_list:
            find_ladders(cur_result + [word], except_set_new, endWord, wordList, result_list)
    result_list = []
    find_ladders([beginWord], {beginWord}, endWord, set(wordList), result_list)
    return result_list

import copy
def findLadders2(beginWord: str, endWord: str, wordList: list) -> list:
    """
    比第一个方法降低了复杂度，将遍历wordList改为遍历26个字母，尝试修改word，然后看是否在wordList中。
    时间复杂度为 O(nl)，其中 l 为单词长度，n 为词序列长度。
    """
    if endWord not in wordList:
        return []
    def dict_add_word(word, d):
        """
        将一个词融入到字典中
        """
        for i in range(len(word)):
            if word[i] not in d:
                d[word[i]] = {}
            d = d[word[i]]
    def is_in_dict(word, d):
        """
        判断word是否在字典中
        """
        for i in range(len(word)):
            if word[i] not in d:
                return False
            d = d[word[i]]
        return True
    def find_ladders(cur_result: list, except_dict: dict, endWord, word_dict: dict, result_list: list):
        """
        递归，以当前转移词序列为基础，继续挑选转移词，直至结束词。
        cur_result:当前转移词序列
        except_set:需要排除的词，不作为候选转移词
        endWord:结束词
        word_dict:词字典，存放词序列的字典形式，便于查询
        result_list:最终结果数组
        """
        # 递归结束条件
        if cur_result[-1] == endWord: # 到达终点
            if not result_list or len(result_list[0]) == len(cur_result):
                result_list.append(cur_result)
            elif len(result_list[0]) > len(cur_result):
                result_list.clear()
                result_list.append(cur_result)
            return
        elif result_list and len(result_list[0]) <= len(cur_result): # 没到达终点，但是长度已经达到了历史最短路径
            return
        # 从词序列中挑选与当前词只差一个字符的词，并按照相似度排序
        next_list = []
        cur_word = cur_result[-1]
        alphabet = [chr(ord('a') + i) for i in range(26)] # 字母表，a-z
        for i in range(len(cur_word)): # 对当前词的每一位依次进行修改
            try_word_list = [cur_word[:i] + x + cur_word[i+1:] for x in alphabet]
            for word in try_word_list:
                if not is_in_dict(word, except_dict) and is_in_dict(word, word_dict):
                    if word[i] == endWord[i]: # 改变字符之后，更接近结束词
                        next_list.insert(0, word) # 优先级高
                    else:
                        next_list.append(word) # 优先级低
        
        if not next_list: # 无候选词，这条路不通
            return
        # 递归继续寻找下一个
        except_dict_new = copy.deepcopy(except_dict) # 候选名单的所有词之后都不必再考虑，否则当前考虑就可以
        for word in next_list:
            dict_add_word(word, except_dict_new)
        for word in next_list:
            find_ladders(cur_result + [word], except_dict_new, endWord, word_dict, result_list)
            
    result_list = []
    word_dict = {}
    for word in wordList:
        dict_add_word(word, word_dict)
    except_dict = {}
    dict_add_word(beginWord, except_dict)
    find_ladders([beginWord], except_dict, endWord, word_dict, result_list)
    return result_list

import collections,string
def findLadders3(begin, end, words_list):
    """
    BFS + DFS
    先用BFS，遍历单词之间的关联，放到字典中
    再用DFS，遍历字典得到从起始到终点的路径
    """
    def construct_paths(source, dest, tree):
        '''
        递归构造从source到dest的所有路径，DFS。
        '''
        if source == dest: 
            return [[source]]
        
        # 以下等价于： return [[source] + path for succ in tree[source] for path in construct_paths(succ, dest, tree)]
        result = []
        for succ in tree[source]:
            for path in construct_paths(succ, dest, tree):
                result.append([source] + path)
        return result

    def add_path(tree, word, neigh, is_forw):
        '''
        为一个节点的下一步增添一个节点
        '''
        if is_forw:
            tree[word] += neigh,
        else:
            tree[neigh] += word,

    def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
        '''
        将words_set中的所有节点构造出父子关系，并存储到tree中。
        this_lev: 当前tree的层，需要构造出this_lev相关的父/子节点
        oth_lev: 与this_lev构造方向相反的层
        tree: 存储所有节点的父子关系，key为父，value为子
        is_forw: 决定需要构造出this_lev相关的父节点节点还是子节点
        words_set: 待加入到tree中的词集
        return: this_lev和oth_lev是否已经对接上
        '''
        if not this_lev:
            return False
        # 优先构造较小集合的下一层
        if len(this_lev) > len(oth_lev): 
            return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
        # 将候选集合剔除掉已有节点
        for word in (this_lev | oth_lev):
            words_set.discard(word)
        # 构造this_lev的next_lev
        next_lev, done = set(), False
        while this_lev:
            word = this_lev.pop()
            for c in string.ascii_lowercase: # 遍历 a-z
                for index in range(len(word)): # 尝试改变单词的每个字符
                    neigh = word[:index] + c + word[index+1:]
                    if neigh in oth_lev: # 已经到达oth_lev
                        done = True
                        add_path(tree, word, neigh, is_forw)                
                    if not done and neigh in words_set:
                        next_lev.add(neigh)
                        add_path(tree, word, neigh, is_forw)
        return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)
                        
    tree = collections.defaultdict(list)
    bfs_level(set([begin]), set([end]), tree, True, set(words_list))
    return construct_paths(begin, end, tree)

if '__main__' == __name__:
    beginWord = "cet"
    endWord = "ism"
    wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    print(findLadders3(beginWord, endWord, wordList))
    
