#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import datetime
import os
import subprocess
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/<url_item>")
def url(url_item):

    if url_item == "network":
        proc = subprocess.Popen(["./network.sh eth0", ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        eth_ip=out

        proc = subprocess.Popen(["./network.sh wlan0", ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        wlan_ip=out

    templateData = {
        'eth_ip': eth_ip,
        'wlan_ip': wlan_ip
    }
    return render_template('network.htm',**templateData)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
