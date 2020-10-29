from flask import Flask, render_template, request, jsonify
from random import choice
from googletrans import Translator
import json

translator = Translator()

web_site = Flask(__name__)


@web_site.route('/translate/', methods=['POST']) 
def test():
    data = request.json
    string = (data["data"])
    translate_to = data["translate_to"]
    #print(string)
    # #return jsonify(data)
    result = translator.translate(string, dest=translate_to)
    #print(result)
    data_set = {"result": result.text,"src":result.src,"pronunciation":result.pronunciation}
    json_dump = json.dumps(data_set,ensure_ascii=False)
    return json_dump
    


web_site.run(host='0.0.0.0', port=8080)