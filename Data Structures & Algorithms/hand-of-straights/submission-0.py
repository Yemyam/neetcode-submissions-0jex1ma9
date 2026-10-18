from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if n groups of groupSize is even possible
        if (len(hand) % groupSize) != 0:
            return False
        
        counts = Counter(hand)
        print(counts)
        # take the min in in the hand and attempt to create a straight of group size from it using the hashmap
        # if its not possible return False, otherwise if all straights can be created return True

        while counts:
            curr_hand = 1
            start = min(counts.keys())
            counts[start] -= 1
            if counts[start] == 0:
                del counts[start]
            curr = start
            while curr_hand < groupSize:
                if (curr + 1) not in counts:
                    return False
                # else add that card into the straight
                counts[curr + 1] -= 1
                if counts[curr + 1] == 0:
                    del counts[curr + 1]
                curr_hand += 1
                curr += 1
        return True