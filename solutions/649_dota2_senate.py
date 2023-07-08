from collections import Counter


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        live_counts = Counter(senate)
        can_kill_counts = Counter()
        chars = [*senate]
        i = 0
        while True:
            c = chars[i]

            if c == "R":
                if can_kill_counts["R"] > 0:
                    chars[i] = ""
                    live_counts["R"] -= 1
                    can_kill_counts["R"] -= 1
                elif live_counts["D"] == 0:
                    return "Radiant"
                else:
                    can_kill_counts["D"] += 1
            elif c == "D":
                print(can_kill_counts, live_counts)
                if can_kill_counts["D"] > 0:
                    chars[i] = ""
                    live_counts["D"] -= 1
                    can_kill_counts["D"] -= 1
                elif live_counts["R"] == 0:
                    return "Dire"
                else:
                    can_kill_counts["R"] += 1

            i = (i + 1) % len(senate)


s = Solution()
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))
print(s.predictPartyVictory("RDDRD"))
