class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # mutations = 0
        # queue = deque([(startGene, mutations)])
        # visited = set()
        # avaliable = "ACGT"
        # visited.add(startGene)

        # while queue:
        #     currgene, mutations = queue.popleft()
        #     print(queue, visited)
        #     if currgene == endGene:
        #         return mutations

        #     for i in range(len(currgene)):
        #         modify = list(currgene)
        #         for chromosome in avaliable:
        #             if modify[i] != chromosome:
        #                 modify[i] = chromosome
        #                 nextgene = "".join(modify)
        #                 if nextgene not in visited and nextgene in bank:
        #                     queue.append((nextgene, mutations + 1))
        #                     visited.add(nextgene)

        # return -1
        
        mutations = 0
        queue = deque([(startGene, mutations)])
        visited = set()
        avaliable = "ACGT"
        visited.add(startGene)


        def check(given, make):
            count = 0
            for i in range(len(given)):
                if given[i] == make[i]:
                    count += 1
            return count
        while queue:
            currgene, mutations = queue.popleft()
            for ava in bank:
                count = check(currgene, ava)
                if count == len(ava) and ava == endGene:
                    return mutations
                elif count == len(ava) - 1 and ava not in visited:
                    queue.append((ava, mutations + 1))
                    visited.add(ava)

        return -1
        