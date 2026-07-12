import math
class Solution:
    def hasGroupsSizeX(self, deck: list) -> bool:
        if len(deck) == 1: return False
        unique_deck = set(deck)
        deck_info = dict()
        # a deck can be described as a scalar multiplication of each card
        for card in unique_deck:
            deck_info[card] = deck.count(card)
        vals_list = list(deck_info.values())
        print(vals_list)
        for i in range(len(vals_list) - 1):
            current_gcd = math.gcd(vals_list[i], vals_list[i + 1])
            print(f"GCD of {vals_list[i]} and {vals_list[i + 1]} is {math.gcd(vals_list[i], vals_list[i + 1])}")
            vals_list[i + 1] = current_gcd
            if i == len(vals_list) - 2 and current_gcd == 1: return False
        return True
    


s = Solution()
deck = [1,1,2,2,2,3,3,3,3,3,3]
print(s.hasGroupsSizeX(deck))