# 🤖 StudBot - AI Learning Companion

**Enter the World of Artificial Intelligence with StudBot**

A comprehensive AI learning platform designed specifically for BSc IT students studying Artificial Intelligence. StudBot provides interactive conversations, practice quizzes, and personalized guidance to help you master AI concepts.

![StudBot Preview](https://via.placeholder.com/800x400/6366f1/ffffff?text=StudBot+AI+Learning+Companion)

## ✨ Features

### 🎯 **Interactive AI Chat**
- Ask questions about any AI concept
- Get detailed, educational responses in **5-mark examination format**
- Quick question buttons for common topics
- Real-time conversation with StudBot
- Structured answers with Introduction, Main Points, and Conclusion

### 📚 **Comprehensive Knowledge Base**
- 500+ AI questions and answers
- 33 different AI topics covered
- 5 complete units of study
- Expert-level explanations

### 🧠 **Practice Quizzes**
- Multiple choice questions with **5-mark examination format answers**
- Three difficulty levels (Easy, Medium, Hard)
- Instant feedback and detailed explanations
- Progress tracking and scoring
- Academic-style structured responses

### 🎨 **Modern UI/UX**
- Beautiful, responsive design
- Smooth animations and transitions
- Professional brand identity
- Mobile-friendly interface

### 🚀 **Easy Deployment**
- Ready for GitHub Pages
- Vercel deployment support
- No complex setup required

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask
- **Styling**: Custom CSS with animations
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)
- **Deployment**: GitHub Pages / Vercel / Heroku / Railway
- **Answer Format**: 5-Mark Examination Style

## 📦 Installation & Setup

### Option 1: Quick Start (Static Version)
1. Clone the repository:
```bash
git clone https://github.com/yourusername/studbot.git
cd studbot
```

2. Open `index.html` in your browser
3. Start learning with StudBot!

### Option 2: Full Backend (Recommended)

#### Windows Users:
1. Double-click `start_studbot.bat`
2. Wait for the server to start
3. Browser will open automatically to http://localhost:5000

#### Linux/Mac Users:
1. Run: `./start_studbot.sh`
2. Wait for the server to start
3. Open http://localhost:5000 in your browser

#### Manual Setup:
1. Clone the repository:
```bash
git clone https://github.com/yourusername/studbot.git
cd studbot
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python app.py
```

4. Open http://localhost:5000 in your browser

## 🚀 Deployment

### GitHub Pages
1. Push your code to GitHub
2. Go to repository Settings > Pages
3. Select source branch (usually `main`)
4. Your site will be available at `https://yourusername.github.io/studbot`

### Vercel
1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Follow the prompts to deploy

## 📚 Knowledge Base

StudBot includes comprehensive coverage of:

### Unit 1: Introduction to AI
- AI Definition and Significance
- Types of AI (Narrow vs General)
- Turing Test and AI Approaches
- Human Brain vs Computer
- AI Foundations and History

### Unit 2: Search Algorithms
- Problem-Solving Agents
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform Cost Search
- A* Search Algorithm
- Hill Climbing
- Genetic Algorithms
- Simulated Annealing

### Unit 3: Adversarial Search & Knowledge
- Minimax Algorithm
- Alpha-Beta Pruning
- Knowledge-Based Agents
- Logic Types
- Probabilistic Reasoning

### Unit 4: First-Order Logic
- FOL Basics and Syntax
- Quantifiers (Universal & Existential)
- Unification
- Forward/Backward Chaining

### Unit 5: Planning & Generative AI
- Classical Planning
- HTN Planning
- Generative AI Models
- Real-world Applications

## 🎯 Usage

### Chat with StudBot
1. Click on the "Chat" section
2. Type your question about AI
3. Get instant, detailed responses
4. Use quick question buttons for common topics

### Take Quizzes
1. Go to the "Quiz" section
2. Choose your difficulty level
3. Answer multiple choice questions
4. Get instant feedback and explanations
5. Track your progress and score

### Explore Topics
- Browse through different AI categories
- Learn at your own pace
- Practice with interactive quizzes
- Master concepts through repetition

## 🎨 Customization

### Adding New Questions
1. Edit `ai_qa_dataset.json`
2. Add new Q&A pairs with proper structure
3. Include relevant keywords and categories
4. Restart the server to load new data

### Styling
- Modify `styles.css` for visual changes
- Update color scheme in CSS variables
- Add new animations and effects
- Customize the robot character

### Functionality
- Extend `script.js` for new features
- Add new API endpoints in `app.py`
- Implement additional quiz types
- Add user authentication if needed

## 📊 Data Structure

### Q&A Format
```json
{
  "id": 1,
  "question": "What is Artificial Intelligence?",
  "answer": "Detailed explanation...",
  "category": "Introduction to AI",
  "marks": 5,
  "keywords": ["AI definition", "intelligence", "machines"],
  "created_at": "2025-01-01T00:00:00"
}
```

### MCQ Format
```json
{
  "id": 1,
  "question": "Who coined the term 'Artificial Intelligence'?",
  "options": {
    "A": "Alan Turing",
    "B": "John McCarthy",
    "C": "Marvin Minsky",
    "D": "Herbert Simon"
  },
  "correct_answer": "B",
  "explanation": "John McCarthy coined 'Artificial Intelligence'...",
  "category": "Introduction to AI",
  "difficulty": "easy"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- AI knowledge base compiled from academic sources
- UI/UX inspired by modern educational platforms
- Icons provided by Font Awesome
- Fonts from Google Fonts

## 📞 Support

- 📧 Email: support@studbot.ai
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/studbot/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/studbot/discussions)

## 🔮 Future Enhancements

- [ ] User authentication and progress tracking
- [ ] Advanced AI models integration
- [ ] Voice interaction capabilities
- [ ] Mobile app development
- [ ] Collaborative learning features
- [ ] Advanced analytics and insights
- [ ] Multi-language support
- [ ] Offline mode support

---

**Made with ❤️ for AI learners everywhere**

*StudBot - Your intelligent companion in the world of Artificial Intelligence*
