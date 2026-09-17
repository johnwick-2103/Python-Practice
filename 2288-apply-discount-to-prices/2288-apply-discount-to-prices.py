class Solution:
    def discountPrices(self, sentence, discount):
        words = sentence.split()

        for i in range(len(words)):
            word = words[i]

            if word.startswith('$') and word[1:].isdigit():
                price = int(word[1:])

                price = price * (100 - discount) / 100

                words[i] = '$' + format(price, '.2f')

        return ' '.join(words)