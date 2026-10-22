import unittest,random
from clock_window_envelope import run
class DomainTests(unittest.TestCase):
 def test_robust_intersection(self):
  r=run({'parties':[{'id':'a','windows':[[0,20]],'offset':[-2,3]},{'id':'b','windows':[[5,19]],'offset':[-1,1]}]});self.assertEqual(r['robust_windows'],[[6,17]])
 def test_adjacent_windows_merged_before_erosion(self):
  self.assertEqual(run({'parties':[{'id':'a','windows':[[0,5],[5,10]],'offset':[-1,1]}]})['robust_windows'],[[1,9]])
 def test_nominal_overlap_not_robust(self):
  r=run({'parties':[{'id':'a','windows':[[0,2]],'offset':[-2,2]}]});self.assertEqual(r['nominal_windows'],[[0,2]]);self.assertIsNone(r['witness_time'])
 def test_discrete_universal_oracle(self):
  rng=random.Random(13)
  for _ in range(40):
   a=rng.randrange(-5,5);b=a+rng.randrange(1,15);lo=rng.randrange(-3,1);hi=rng.randrange(0,4)
   r=run({'parties':[{'id':'a','windows':[[a,b]],'offset':[lo,hi]}]})
   for t in range(-10,25):self.assertEqual(any(x<=t<y for x,y in r['robust_windows']),all(a<=t+o<b for o in range(lo,hi+1)))
 def test_offset_order(self):
  with self.assertRaises(ValueError):run({'parties':[{'id':'a','windows':[[0,5]],'offset':[2,1]}]})
