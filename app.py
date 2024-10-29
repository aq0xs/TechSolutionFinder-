from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-solution', methods=['POST'])
def get_solution():
    data = request.get_json()
    problem = data['problem']
    
    # هنا يمكنك وضع منطق تحليل المشكلة وتوليد الحل
    solution = f"الحل لمشكلتك '{problem}' هو: تأكد من إعادة تشغيل الجهاز."
    
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)
