"""
This script runs the node_analytics application using a development server.
"""

from os import environ
from node_analytics import app

if __name__ == '__main__':
    app.run(port='5002')