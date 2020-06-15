"""
This script runs the node_AC application using a development server.
"""

from os import environ
from node_AC import app

if __name__ == '__main__':
    app.run(port='5003')
