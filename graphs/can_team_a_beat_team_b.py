from collections import namedtuple, defaultdict

MatchResult = namedtuple('MatchResult', ('winner', 'looser'))


class Solution(object):

    def build_graph(self, matches):
        graph = defaultdict(set)
        for match in matches:
            graph[match.winner].add(match.looser)
        return graph

    def is_reachable(self, graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(self.is_reachable(graph, team, dest, visited) for team in graph[curr])

    def can_team_a_beat_team_b(self, matches, team_a, team_b):
        return self.is_reachable(self.build_graph(matches), team_a, team_b)


if __name__ == '__main__':
    matches =[ MatchResult('1','2'),
              MatchResult('11','21'),
              MatchResult('111','211'),
              MatchResult('2','211')]
    print(Solution().can_team_a_beat_team_b(matches,'1', '211'))
