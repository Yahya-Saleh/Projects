# TideMan
Tideman implements a ranked-choice system. In a ranked-choice system, voters can vote for more than one candidate. Instead of just voting for their top choice, they can rank the candidates in order of preference. The winner then is   the person who would have won any head-to-head matchup against another candidate- the so-called “Condorcet winner” of the election.

 As ranked ballot-1.png shows an election that would have ended in tie between Alice and Bob will now end in Alice winning because the voter who voted for Charlie prefers her over Bob.

 Generally speaking, the Tideman method works by constructing a “graph” of candidates, where an arrow (i.e. edge) from candidate A to candidate B indicates that candidate A wins against candidate B in a head-to-head matchup. the graph for condorcet.png is shown in condorcet-graph.png

 ## Usage
 