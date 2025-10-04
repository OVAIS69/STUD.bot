# 🚀 Deploy StudBot on Vercel - Complete Guide

## 📋 Prerequisites

- GitHub account
- Vercel account (free at [vercel.com](https://vercel.com))
- Your StudBot code pushed to GitHub

## 🌐 Method 1: Deploy via Vercel Dashboard (Recommended)

### Step 1: Prepare Your Repository
1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Deploy StudBot to Vercel"
   git push origin main
   ```

### Step 2: Connect to Vercel
1. **Go to Vercel Dashboard**
   - Visit [vercel.com](https://vercel.com)
   - Sign up/Login with your GitHub account

2. **Import Project**
   - Click "New Project"
   - Select "Import Git Repository"
   - Choose your StudBot repository
   - Click "Import"

### Step 3: Configure Build Settings
1. **Project Settings**
   - **Project Name**: `studbot-ai-learning` (or your preferred name)
   - **Framework Preset**: `Other`
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: `./` (leave as default)
   - **Install Command**: `pip install -r requirements.txt`

2. **Environment Variables** (Optional)
   - Add if needed:
     ```
     FLASK_ENV=production
     PORT=5000
     ```

3. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (2-3 minutes)

### Step 4: Access Your Deployed App
- Your app will be available at: `https://studbot-ai-learning.vercel.app`
- Vercel will provide you with a custom URL

## 🔧 Method 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy from Project Directory
```bash
cd studbot
vercel
```

### Step 4: Follow the Prompts
```
? Set up and deploy "~/studbot"? [Y/n] y
? Which scope do you want to deploy to? Your Personal Account
? Link to existing project? [y/N] n
? What's your project's name? studbot-ai-learning
? In which directory is your code located? ./
? Want to override the settings? [y/N] n
```

### Step 5: Production Deployment
```bash
vercel --prod
```

## ⚙️ Vercel Configuration File

Create a `vercel.json` file in your project root:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "FLASK_ENV": "production"
  }
}
```

## 🔍 Troubleshooting Common Issues

### Issue 1: Build Fails
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**: Ensure `requirements.txt` includes all dependencies:
```
Flask==2.3.3
flask-cors==4.0.0
```

### Issue 2: App Doesn't Start
**Error**: App shows "Application Error"

**Solution**: Update `app.py` for Vercel:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Issue 3: Static Files Not Loading
**Error**: CSS/JS files return 404

**Solution**: Add static file handling in `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    },
    {
      "src": "static/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

## 📱 Testing Your Deployment

### 1. Test Main Page
- Visit your Vercel URL
- Check if the homepage loads correctly

### 2. Test Chat Functionality
- Go to Chat section
- Ask a question like "What is AI?"
- Verify you get a 5-mark format response

### 3. Test MCQ Quizzes
- Go to Quiz section
- Try all difficulty levels (Easy, Medium, Hard)
- Verify questions load and answers work

### 4. Test API Endpoints
```bash
# Test stats endpoint
curl https://your-app.vercel.app/api/stats

# Test quiz endpoint
curl https://your-app.vercel.app/api/quiz/easy

# Test chat endpoint
curl -X POST https://your-app.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is AI?"}'
```

## 🔄 Updating Your Deployment

### Method 1: Automatic Updates
- Push changes to your GitHub repository
- Vercel will automatically redeploy

### Method 2: Manual Redeploy
```bash
vercel --prod
```

## 📊 Vercel Features You Get

### Free Tier Includes:
- ✅ Unlimited personal projects
- ✅ 100GB bandwidth per month
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Custom domains
- ✅ Automatic deployments from GitHub

### Performance:
- ✅ Fast global deployment
- ✅ Automatic scaling
- ✅ Edge functions support
- ✅ Real-time analytics

## 🎯 Final Checklist

Before deploying, ensure:
- [ ] All files are committed to GitHub
- [ ] `requirements.txt` includes all dependencies
- [ ] `vercel.json` is configured (optional but recommended)
- [ ] Flask app is configured for production
- [ ] All API endpoints work locally
- [ ] Static files (CSS, JS) are accessible

## 🚀 Post-Deployment

After successful deployment:
1. **Share your URL** with users
2. **Monitor performance** in Vercel dashboard
3. **Set up custom domain** (optional)
4. **Enable analytics** to track usage
5. **Set up monitoring** for uptime

## 📞 Support

If you encounter issues:
1. Check Vercel deployment logs
2. Verify all dependencies are in `requirements.txt`
3. Test API endpoints individually
4. Check Vercel documentation: [vercel.com/docs](https://vercel.com/docs)

Your StudBot will be live at: `https://your-project-name.vercel.app`
