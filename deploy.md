# 🚀 StudBot Deployment Guide

This guide will help you deploy StudBot to various platforms.

## 📋 Prerequisites

- GitHub account
- Python 3.7+ installed locally
- Git installed

## 🌐 Deployment Options

### Option 1: GitHub Pages (Static Version)

**Best for**: Simple static deployment, no backend needed

1. **Fork/Clone the repository**
   ```bash
   git clone https://github.com/yourusername/studbot.git
   cd studbot
   ```

2. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click on "Settings" tab
   - Scroll down to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch
   - Click "Save"

4. **Access your site**
   - Your site will be available at: `https://yourusername.github.io/studbot`
   - It may take a few minutes to deploy

### Option 2: Vercel (Full Backend)

**Best for**: Full functionality with Python backend

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy from project directory**
   ```bash
   cd studbot
   vercel
   ```

4. **Follow the prompts**
   - Project name: `studbot`
   - Framework: `Other`
   - Build command: `python app.py`
   - Output directory: `./`

5. **Access your site**
   - Vercel will provide you with a URL
   - Example: `https://studbot-abc123.vercel.app`

### Option 3: Heroku (Full Backend)

**Best for**: Production deployment with database

1. **Install Heroku CLI**
   - Download from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create studbot-ai-learning
   ```

4. **Add Python buildpack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Open your app**
   ```bash
   heroku open
   ```

### Option 4: Netlify (Static + Functions)

**Best for**: Static site with serverless functions

1. **Connect to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository

2. **Configure build settings**
   - Build command: `echo "No build required"`
   - Publish directory: `./`

3. **Deploy**
   - Click "Deploy site"
   - Your site will be available at a Netlify URL

## 🔧 Configuration

### Environment Variables

For production deployment, you may want to set these environment variables:

```bash
FLASK_ENV=production
FLASK_DEBUG=False
```

### Custom Domain (Optional)

1. **GitHub Pages**
   - Add `CNAME` file with your domain
   - Configure DNS settings

2. **Vercel**
   - Go to project settings
   - Add custom domain
   - Configure DNS

3. **Heroku**
   - Use Heroku CLI to add domain
   - Configure DNS settings

## 📊 Monitoring

### GitHub Pages
- Check deployment status in repository settings
- View build logs for any issues

### Vercel
- Monitor deployments in Vercel dashboard
- Check function logs for backend issues

### Heroku
- Use `heroku logs --tail` to monitor
- Check Heroku dashboard for metrics

## 🐛 Troubleshooting

### Common Issues

1. **Build Failures**
   - Check Python version compatibility
   - Ensure all dependencies are in requirements.txt
   - Verify file paths are correct

2. **CORS Issues**
   - Make sure Flask-CORS is installed
   - Check CORS configuration in app.py

3. **Static Files Not Loading**
   - Verify file paths in HTML/CSS
   - Check if files are in correct directories

4. **Database Issues**
   - Ensure database files are included
   - Check file permissions

### Debug Mode

For local development:
```bash
export FLASK_ENV=development
export FLASK_DEBUG=True
python app.py
```

## 🔄 Updates

### Updating Your Deployment

1. **Make changes locally**
2. **Test locally**
   ```bash
   python app.py
   ```
3. **Commit and push**
   ```bash
   git add .
   git commit -m "Update StudBot"
   git push origin main
   ```
4. **Deployment will update automatically**

## 📈 Performance Optimization

### For Static Sites
- Enable GZIP compression
- Optimize images
- Use CDN for static assets

### For Backend Sites
- Use production WSGI server (Gunicorn)
- Enable caching
- Optimize database queries
- Use environment variables for secrets

## 🛡️ Security

### Best Practices
- Never commit API keys or secrets
- Use environment variables
- Enable HTTPS
- Regular security updates
- Input validation

### Environment Variables
```bash
# .env file (don't commit this)
FLASK_SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

## 📞 Support

If you encounter issues:

1. Check the logs
2. Verify configuration
3. Test locally first
4. Check platform documentation
5. Open an issue on GitHub

## 🎉 Success!

Once deployed, your StudBot will be available to students worldwide!

- **Static Version**: Perfect for showcasing the UI and basic functionality
- **Backend Version**: Full AI chat and quiz functionality

Choose the deployment method that best fits your needs!
