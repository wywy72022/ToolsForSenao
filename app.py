from flask import Flask, request, jsonify
from play_sound import play_sound
from speech_to_text import speech_to_text
from people_count import count_people

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_tool():
    command = request.json.get('command')
    
    if '播放聲音' in command or '喇叭' in command:
        play_sound()
        return jsonify({"message": "播放聲音成功"})
    
    elif '語音轉文字' in command or 'STT' in command:
        result = speech_to_text()
        return jsonify({"message": "語音轉文字完成", "text": result})
    
    elif '人數' in command or '鏡頭' in command:
        people_count = count_people()
        return jsonify({"message": "人數偵測完成", "people_count": people_count})
    
    else:
        return jsonify({"message": "無效的命令"}), 400

if __name__ == '__main__':
    app.run(debug=True)
