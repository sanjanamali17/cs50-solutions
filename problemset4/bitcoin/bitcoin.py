import sys
import requests

API_KEY = "YOUR_API_KEY_HERE"

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:

