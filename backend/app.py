from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from utils.code_analyzer import AdvancedCodeAnalyzer

load_dotenv()

app = Flask(__name__)
CORS(app)

analyzer = AdvancedCodeAnalyzer()

@app.route('/')
def home():
    return jsonify({
        "message": "AI Code Reviewer API with Advanced Prompt Framework",
        "version": "2.0",
        "features": [
            "Structured prompt templates",
            "Multiple reviewer perspectives",
            "Quality metrics scoring",
            "Security and performance analysis"
        ]
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Advanced AI Code Reviewer"})

@app.route('/review', methods=['POST'])
def review_code():
    try:
        data = request.get_json()
        
        required_fields = ['code', 'language']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}"
                }), 400
        
        code = data['code']
        language = data['language']
        focus_areas = data.get('focus_areas', ['bugs', 'security', 'performance', 'style', 'best_practices'])
        
        if not code.strip():
            return jsonify({
                "success": False,
                "error": "Code cannot be empty"
            }), 400
        
        result = analyzer.analyze_code(code, language, focus_areas)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/quick-feedback', methods=['POST'])
def quick_feedback():
    try:
        data = request.get_json()
        
        code = data.get('code', '')
        language = data.get('language', 'python')
        
        if not code.strip():
            return jsonify({
                "success": False,
                "error": "Code cannot be empty"
            }), 400
        
        result = analyzer.get_quick_feedback(code, language)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/security-analysis', methods=['POST'])
def security_analysis():
    try:
        data = request.get_json()
        
        code = data.get('code', '')
        language = data.get('language', 'python')
        
        if not code.strip():
            return jsonify({
                "success": False,
                "error": "Code cannot be empty"
            }), 400
        
        result = analyzer.security_analysis(code, language)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/performance-analysis', methods=['POST'])
def performance_analysis():
    try:
        data = request.get_json()

        code = data.get('code', '')
        language = data.get('language', 'python')

        if not code.strip():
            return jsonify({
                "success": False,
                "error": "Code cannot be empty"
            }), 400

        result = analyzer.performance_analysis(code, language)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/sample', methods=['GET'])
def sample():
    return jsonify({
        "message": "Sample API endpoint working!",
        "timestamp": "2024-01-01T00:00:00Z",
        "status": "success"
    })

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"Starting Advanced AI Code Reviewer API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)