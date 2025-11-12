# CodeGuardian Setup Guide

This guide will help you set up and run CodeGuardian on your local machine.

## 🚀 Quick Start

### 1. Get Your OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (you won't be able to see it again!)

### 2. Configure Environment Variables

```bash
# Copy the example environment file
copy .env.example .env

# On Linux/Mac use:
# cp .env.example .env
```

Edit the `.env` file and add your API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
FLASK_PORT=5000
FLASK_ENV=development
```

### 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**Note:** It's recommended to use a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

### 4. Start the Backend Server

```bash
# From the backend directory
python app.py
```

You should see:
```
Starting Advanced AI Code Reviewer API on port 5000
 * Running on http://0.0.0.0:5000
```

### 5. Start the Frontend Server

Open a **new terminal window** and run:

```bash
cd frontend
python -m http.server 3000
```

You should see:
```
Serving HTTP on :: port 3000 (http://[::]:3000/) ...
```

### 6. Access the Application

Open your browser and navigate to:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000/health

## ✅ Verification Checklist

- [ ] Backend server is running on port 5000
- [ ] Frontend server is running on port 3000
- [ ] Browser shows "Connected" status indicator
- [ ] Can paste code and click "Review Code"
- [ ] Receives AI-generated code review

## 🐛 Troubleshooting

### Issue: "OPENAI_API_KEY environment variable is required"

**Solution:** Make sure you've created the `.env` file in the root directory with your API key.

### Issue: "Port already in use"

**Solution:** 
- For backend: Change `FLASK_PORT` in `.env` to a different port (e.g., 5001)
- For frontend: Use a different port: `python -m http.server 3001`

### Issue: "Module not found" errors

**Solution:** Make sure you've installed all dependencies:
```bash
cd backend
pip install -r requirements.txt
```

### Issue: Frontend shows "Disconnected"

**Solution:** 
1. Check if backend is running on port 5000
2. Visit http://localhost:5000/health to verify
3. Check browser console for CORS errors

### Issue: "Invalid API key"

**Solution:** 
1. Verify your API key is correct in `.env`
2. Make sure there are no extra spaces or quotes
3. Check if your OpenAI account has credits

## 📝 Testing the Application

1. **Paste sample code:**
   ```python
   def calculate_average(numbers):
       total = 0
       for i in range(len(numbers)):
           total += numbers[i]
       return total / len(numbers)
   ```

2. **Select language:** Python

3. **Choose focus areas:** Check all boxes

4. **Click "Review Code"**

5. **Wait for results:** Should take 5-10 seconds

## 🔒 Security Notes

- **Never commit your `.env` file** to version control
- The `.gitignore` file is configured to exclude it
- Keep your OpenAI API key private
- Monitor your API usage on the OpenAI dashboard

## 💡 Tips

- Use **Quick Feedback** for faster results (uses GPT-3.5)
- Use **Review Code** for comprehensive analysis (uses GPT-4)
- Export reviews for documentation
- Try different programming languages
- Customize focus areas based on your needs

## 📞 Need Help?

If you encounter issues:
1. Check the terminal output for error messages
2. Verify all prerequisites are installed
3. Ensure your OpenAI API key is valid and has credits
4. Check the browser console for frontend errors

## 🎉 You're All Set!

Your CodeGuardian installation is complete. Start analyzing your code with AI-powered insights!
