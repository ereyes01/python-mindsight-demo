# Python Mindsight Demo

This program will do some busy work that will eventually produce some data in your Mindsight account. Note that it relies on the behavior of `input()` in Python 2 as it's currently written.

It'll ask you to enter a number that approximates how hard the program should work. Entering about `50000` should make it spin long enough to generate some data.

To run this program:

- Start the [Mindsight Agent](https://github.com/MindsightCo/hotpath-agent) with your credentials
  - Program assumes that it's running on http://localhost:8000/
- Install the Python Mindsight client:
  - `pip install -U mindsight-sampler`
- Run the program:
  - `python main.py` 
  
