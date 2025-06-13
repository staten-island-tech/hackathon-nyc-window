from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API = ""
cached_data = []
