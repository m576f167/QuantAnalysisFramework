""" Entry point for the application  """

import sys
from app import create_app

def main(argv):
    app = create_app()

if __name__ == '__main__':
    main(sys.argv[1:])
