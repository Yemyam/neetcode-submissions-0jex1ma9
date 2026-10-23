class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we can store a cooldown array, where each element is [task, remaining_cooldown]
        # we can construct a max heap of [tasks_remaining, task_name]
        freqs = {}
        total = 0
        out = 0
        for task in tasks:
            freqs[task] = 1 + freqs.get(task, 0)
            total += 1
        # freqs now contains a hashmap of the frequency of each task
        # we want to generate a max heap so we negate the count for each item
        heap = [[-task[1], task[0]] for task in freqs.items()]
        heapq.heapify(heap)
        # create a q for the cooldown of each task
        cooldowns = collections.deque()
        while len(cooldowns) < n + 1:
            cooldowns.append("")
        print(heap)
        while total > 0:
            out += 1
            # pop the last cooldown from the q
            task = cooldowns.popleft()
            if task != "":
                if task[0] != 0:
                    heapq.heappush(heap, task)
            if heap:
                task = heapq.heappop(heap)
                total -= 1
                task[0] += 1
                cooldowns.append(task)
            if len(cooldowns) < n + 1:
                cooldowns.append("")
        return out
