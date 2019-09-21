def uniqueMorseRepresentations(words):
        alph = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list = set()
        for word in words:
            res = ''
            for ch in word:
                res = res + (alph[ord(ch) - ord('a')])
            list.add(res)

        return len(list)


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

            
