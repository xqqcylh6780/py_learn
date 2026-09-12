import io
import unittest
from contextlib import redirect_stdout
from demo_app.cli import main

class CliTests(unittest.TestCase):
    def test_hello(self):
        out=io.StringIO()
        with redirect_stdout(out):
            code=main(["Alice"])
        self.assertEqual(code,0)
        self.assertEqual(out.getvalue().strip(),"hello Alice")

if __name__ == "__main__":
    unittest.main()
