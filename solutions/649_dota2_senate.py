from collections import Counter, deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        live_counts = Counter(senate)
        can_kill_counts = Counter()
        chars = deque(senate)
        while live_counts["D"] and live_counts["R"]:
            c = chars.popleft()

            if c == "R":
                if can_kill_counts["R"] > 0:
                    live_counts["R"] -= 1
                    can_kill_counts["R"] -= 1
                else:
                    can_kill_counts["D"] += 1
                    chars.append(c)
            elif c == "D":
                if can_kill_counts["D"] > 0:
                    live_counts["D"] -= 1
                    can_kill_counts["D"] -= 1
                else:
                    can_kill_counts["R"] += 1
                    chars.append(c)

        return "Dire" if live_counts["D"] else "Radiant"


s = Solution()
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))
print(s.predictPartyVictory("RDDRD"))
