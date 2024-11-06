class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        mutations = 0
        queue = deque([(startGene, mutations)])
        visited = set()
        avaliable = "ACGT"
        visited.add(startGene)

        while queue:
            currgene, mutations = queue.popleft()
            print(queue, visited)
            if currgene == endGene:
                return mutations

            for i in range(len(currgene)):
                modify = list(currgene)
                print("modify: ", modify, "at ", i)
                for chromosome in avaliable:
                    if modify[i] != chromosome:
                        modify[i] = chromosome
                        nextgene = "".join(modify)
                        print("modified->", nextgene)
                        if nextgene not in visited and nextgene in bank:
                            print("Added->", nextgene)
                            queue.append((nextgene, mutations + 1))
                            visited.add(nextgene)

        return -1
        