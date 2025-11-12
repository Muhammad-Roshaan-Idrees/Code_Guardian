from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
from utils.code_analyzer import AdvancedCodeAnalyzer

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}})

analyzer = AdvancedCodeAnalyzer()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Advanced AI Code Reviewer"})

@app.route('/review', methods=['POST'])
def review_code():
    try:
        data = request.get_json()
        if not data or 'code' not in data or 'language' not in data:
            return jsonify({"success": False, "error": "Missing required fields"}), 400
        
        code = data['code']
        language = data['language']
        focus_areas = data.get('focus_areas', ['bugs', 'security', 'performance', 'style', 'best_practices'])
        
        if not code.strip():
            return jsonify({"success": False, "error": "Code cannot be empty"}), 400
        
        result = analyzer.analyze_code(code, language, focus_areas)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/quick-feedback', methods=['POST'])
def quick_feedback():
    try:
        data = request.get_json()
        if not data or 'code' not in data:
            return jsonify({"success": False, "error": "Missing required fields"}), 400
        
        code = data['code']
        language = data.get('language', 'python')
        if not code.strip():
            return jsonify({"success": False, "error": "Code cannot be empty"}), 400
        
        result = analyzer.get_quick_feedback(code, language)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/security-analysis', methods=['POST'])
def security_analysis():
    try:
        data = request.get_json()
        code = data.get('code', '')
        language = data.get('language', 'python')
        if not code.strip():
            return jsonify({"success": False, "error": "Code cannot be empty"}), 400
        
        result = analyzer.security_analysis(code, language)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/performance-analysis', methods=['POST'])
def performance_analysis():
    try:
        data = request.get_json()
        code = data.get('code', '')
        language = data.get('language', 'python')
        if not code.strip():
            return jsonify({"success": False, "error": "Code cannot be empty"}), 400
        
        result = analyzer.performance_analysis(code, language)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    print(f"Starting Advanced AI Code Reviewer API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
