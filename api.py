from flask import Flask, render_template, request, jsonify
from math import sqrt
import requests
import hashlib
import os

#Api funtions
def fact(n):
	if n > 0:
		return n * fact(n-1)
	else:
		return 1
	
