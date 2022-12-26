class Anagram:
    def __init__(self, word):
        self.sorted_letter = sorted([ each_let for each_let in word])

        #print(self.sorted_letter)

    def match(self, list_arr):
        result = []
        for each_word in list_arr:
            #print(each_word)
            if(sorted([each_let for each_let in each_word]) == self.sorted_letter):
                result.append(each_word)
        
        print(result)
        return result
                


new_word = Anagram("enlist")
new_word.match(["listen", "poison", "hello"])