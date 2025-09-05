class Solution(object):
    def minimumCardPickup(self, cards):
        cardSet, l, min_cards = set(), 0, 0
        for r in range(len(cards)):
            while cards[r] in cardSet:
                min_cards = (r - l + 1) if min_cards == 0 else min(min_cards, r - l + 1)
                cardSet.remove(cards[l])
                l = l + 1
            cardSet.add(cards[r])
        
        return -1 if min_cards == 0 else min_cards

        