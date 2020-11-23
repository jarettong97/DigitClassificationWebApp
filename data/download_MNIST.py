import os
import requests

if "mnist.pkl.gz" not in os.listdir():
    r = requests.get("http://deeplearning.net/data/mnist/mnist.pkl.gz")
    with open("mnist.pkl.gz", 'wb') as f:
        f.write(r.content)