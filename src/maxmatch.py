# encode:utf-8

import argparse


class MaxMatch:
    """
        句子的最大匹配

    """


    class WordNode:
        """
            保存词语字典
        """
        wordMap = {}

        def __init__(self, word):
            self.word = word
            self.next_words = []
            if self.wordMap.get(word) is None:
                self.wordMap[word] = self

        def add_next(self, word_node):
            self.next_words.append(word_node.word)

        def __str__(self):
            next_str = ""
            for n in self.next_words:
                next_str += n+" "
            return self.word+"->["+next_str+"]"

    def __init__(self):
        pass

    def read_corpus(self, corpus_file):
        """
            读取语料，生成词典
        :param corpus_file: 语料文件路径
        :return:
        """
        f = open(corpus_file)
        lines = f.readlines()
        for l in lines:
            word_array = l.replace("\n", "").split(" ")
            last = None
            for w in word_array:
                node = self.WordNode.wordMap.get(w)
                if node is None:
                    node = self.WordNode(w)
                if last is not None:
                    last.add_next(node)
                last = node

    def dis_corpus_map(self):
        """
            显示根据语料生成的词典
        :return:
        """
        print("---------------------------")
        for w in self.WordNode.wordMap:
            next_str = ""
            words = self.WordNode.wordMap[w].next_words
            for l in words:
                next_str+=" "+l
            print(w+":["+next_str+"]")
        print("---------------------------")

    def match(self, sentence):
        """
            进行最大匹配
        :param sentence:
        :return: 匹配结果，形如：[['⼩明'], ['是'], ['复旦', '⼤学', '的', '学⽣']]
        """
        words = sentence.split(" ")
        results = self.get_match_result(words)
        # print(results)
        matches = self.extract_result(results, words)
        return matches

    def get_match_result(self, words):
        """
            获取匹配结果
        :param words: 词语数组
        :return: 匹配结果，形如[-1 0 1 1 1]
        """
        result = []
        next_words = []
        for w in words:
            word = self.WordNode.wordMap.get(w)
            # if word is a new word
            if word is None:
                # print("new")
                result.append(-1)
                continue

            if w in next_words:
                result.append(1)
                # print("match")
            else:
                result.append(0)
                # print("new match")

            next_words = word.next_words

        return result

    @staticmethod
    def extract_result(result, words):
        """
            提取匹配结果
        :param result: 匹配结果数组，如[1, 0, 0, -1]
        :param words: 词语数组
        :return: 匹配结果
        """
        matches = []
        i = 0
        while i < len(result):
            if result[i] == -1:
                matches.append([words[i]])
                i += 1
                continue
            if result[i] == 0:
                new_match = []
                new_match.append(words[i])
                i += 1
                while i<len(result) and result[i]==1:
                    new_match.append(words[i])
                    i += 1
                matches.append(new_match)
        return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",   default="./data/corpus",
                        dest="corpus",
                        help="corpus file path")
    parser.add_argument("sentence")
    parser.add_argument("-o", dest="output_path", help="output file path")
    args = parser.parse_args()

    matcher = MaxMatch()
    matcher.read_corpus(args.corpus)
    # matcher.dis_corpus()
    print(matcher.match(args.sentence))

