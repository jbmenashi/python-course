import unittest
from unittests import eat

class UnittestTests(unittest.TestCase):
   def test_eat_healthy(self):
      self.assertEqual(
         eat("broccoli", is_healthy=True),
         "I'm eating broccoli, it's so healthy"
      )

   def test_eat_unhealthy(self):
      self.assertEqual(
         eat("pizza", is_healthy=False),
         "I'm eating pizza, it's so unhealthy"
      )

if __name__ == "__main__":
   unittest.main()
