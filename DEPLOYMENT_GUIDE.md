# 🚀 StudBot Deployment Guide

## 📋 Quick Start

### Option 1: Local Development (Recommended for Testing)

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   - Open your browser and go to: `http://localhost:5000`
   - The application will run with full backend functionality

### Option 2: Static Deployment (GitHub Pages)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy StudBot"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click "Settings" → "Pages"
   - Select "Deploy from a branch"
   - Choose "main" branch
   - Your site will be available at: `https://yourusername.github.io/studbot`

**Note:** Static deployment only provides the UI without backend functionality.

## 🌐 Full Deployment Options

### Option 1: Vercel (Recommended for Full Functionality)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Configure Build Settings**
   - Framework: `Other`
   - Build Command: `pip install -r requirements.txt && python app.py`
   - Output Directory: `./`

### Option 2: Heroku

1. **Install Heroku CLI**
   - Download from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login and Create App**
   ```bash
   heroku login
   heroku create studbot-ai-learning
   ```

3. **Add Python Buildpack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### Option 3: Railway

1. **Connect GitHub Repository**
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub account
   - Select your StudBot repository

2. **Configure Deployment**
   - Railway will auto-detect Python
   - Add environment variables if needed
   - Deploy automatically

### Option 4: Render

1. **Create New Web Service**
   - Go to [render.com](https://render.com)
   - Connect GitHub repository
   - Choose "Web Service"

2. **Configure Settings**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Environment: `Python 3`

## 🔧 Configuration

### Environment Variables

Create a `.env` file for production:
```env
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

### Production Settings

Update `app.py` for production:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

## 📱 Features Available by Deployment Type

| Feature | Local | GitHub Pages | Vercel/Heroku/Railway |
|---------|-------|--------------|----------------------|
| Beautiful UI | ✅ | ✅ | ✅ |
| Interactive Chat | ✅ | ❌ | ✅ |
| MCQ Quizzes | ✅ | ❌ | ✅ |
| Backend API | ✅ | ❌ | ✅ |
| 5-Mark Answer Format | ✅ | ❌ | ✅ |
| Real-time Responses | ✅ | ❌ | ✅ |

## 🐛 Troubleshooting

### Common Issues

1. **MCQ Not Working**
   - Ensure backend is running
   - Check browser console for errors
   - Verify API endpoints are accessible

2. **Chat Not Responding**
   - Check if Flask server is running
   - Verify `/api/chat` endpoint
   - Check network tab in browser dev tools

3. **Deployment Issues**
   - Ensure all dependencies are in `requirements.txt`
   - Check build logs for errors
   - Verify environment variables

### Testing Checklist

- [ ] Backend server starts without errors
- [ ] Frontend loads correctly
- [ ] Chat functionality works
- [ ] MCQ quizzes load and function
- [ ] Answers display in 5-mark format
- [ ] All difficulty levels work
- [ ] Mobile responsiveness

## 📞 Support

If you encounter issues:
1. Check the browser console for JavaScript errors
2. Verify the Flask server is running
3. Test API endpoints directly
4. Check the deployment logs

## 🎯 Next Steps

After successful deployment:
1. Test all functionality
2. Share the URL with users
3. Monitor performance
4. Add more questions to the knowledge base
5. Implement user authentication (optional)
