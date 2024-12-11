import io
import sys
import unittest

from main import interactive


class TestMain(unittest.TestCase):
    """
    Test the main function.
    """

    def setUp(self):
        pass

    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

    def testGraph(self):
        """
        Function to test graph through main function.
        """
        sys.stdin = io.StringIO(
            "gav\nA\ngav\nB\ngdg\ngdv\nA\ngdg\ngae\nA B 2\ngae\nA C 3\ngdg\ngde\nA C\ngdg\ngae\nA D 4\ngdg\ngrn\nA\ngrn\nD\ngae\nB C 3\ngdg\ngcp\nA C\nq"
        )
        capOut = io.StringIO()
        sys.stdout = capOut
        interactive()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        outMsg = capOut.getvalue()
        print(outMsg)
        self.assertIn("Get Path: from A to C { (A,B) (B,C) }", outMsg)

    def testHashTable(self):
        """
        Function to test hash table through main function.
        """
        sys.stdin = io.StringIO(
            "gae\nA B 2\ngae\nA C 3\ngae\nB D 2\ngae\nD E 1\ngae\nC E 4\ngae\nB E 2\ngdg\n"
            + "hi\nh1 A E 30\nhd\nhs\nh1\nhr\nh1\nhd\nq"
        )
        capOut = io.StringIO()
        sys.stdout = capOut
        interactive()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        outMsg = capOut.getvalue()
        print(outMsg)
        self.assertIn("Get Path: from A to E { (A,B) (B,E) }", outMsg)
        self.assertIn(
            "Find vehicle: Vehicle ID: h1 Current Location: A Destination Location: E Distance to Destination: 4 Battery Level: 30",
            outMsg,
        )
        self.assertIn("Delete vehicle: h1 success", outMsg)

    def testRecommend(self):
        """
        Function to test recommend through main function.
        """
        sys.stdin = io.StringIO(
            "gae\nA B 2\ngae\nA C 3\ngae\nB D 2\ngae\nD E 1\n"
            + "gae\nC E 4\ngae\nB E 2\ngae\ngdg\n"
            + "hi\nh1 A E 30\n"
            + "hi\nh2 C E 50\n"
            + "hi\nh3 B D 40\nhd\n"
            + "rnv\nrhb\nq"
        )
        capOut = io.StringIO()
        sys.stdout = capOut
        interactive()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        outMsg = capOut.getvalue()
        print(outMsg)
        self.assertIn("Get Path: from A to E { (A,B) (B,E) }", outMsg)
        self.assertIn("Get Path: from C to E { (C,E) }", outMsg)
        self.assertIn("Get Path: from B to D { (B,D) }", outMsg)
        self.assertIn(
            "Nearest vehicle: Vehicle ID: h3 Current Location: B Destination Location: D Distance to Destination: 2 Battery Level: 40",
            outMsg,
        )
        self.assertIn(
            "Highest battery level vehicle: Vehicle ID: h2 Current Location: C Destination Location: E Distance to Destination: 4 Battery Level: 50",
            outMsg,
        )


if __name__ == "__main__":
    unittest.main()
