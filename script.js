// StudBot - AI Learning Companion
// Main JavaScript functionality

class StudBot {
    constructor() {
        this.currentQuiz = null;
        this.quizQuestions = [];
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.userAnswers = [];
        this.quizTimer = null;
        this.timeLeft = 0;
        
        this.initializeApp();
        this.loadQuizData();
    }

    initializeApp() {
        // Navigation functionality
        this.setupNavigation();
        
        // Chat functionality
        this.setupChat();
        
        // Quiz functionality
        this.setupQuiz();
        
        // Smooth scrolling
        this.setupSmoothScrolling();
        
        // Mobile menu
        this.setupMobileMenu();
        
        // Initialize animations
        this.setupAnimations();
    }

    setupNavigation() {
        const navLinks = document.querySelectorAll('.nav-link');
        const sections = document.querySelectorAll('section');

        // Update active nav link on scroll
        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (scrollY >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });
    }

    setupSmoothScrolling() {
        const links = document.querySelectorAll('a[href^="#"]');
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    setupMobileMenu() {
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');

        if (navToggle && navMenu) {
            navToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
                navToggle.classList.toggle('active');
            });

            // Close menu when clicking on a link
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                });
            });
        }
    }

    setupAnimations() {
        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, observerOptions);

        // Observe elements for animation
        const animateElements = document.querySelectorAll('.section-header, .chat-container, .quiz-welcome, .about-content');
        animateElements.forEach(el => observer.observe(el));
    }

    setupChat() {
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.querySelector('.send-btn');

        // Send message on Enter key
        if (messageInput) {
            messageInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.sendMessage();
                }
            });
        }

        // Send message on button click
        if (sendBtn) {
            sendBtn.addEventListener('click', () => {
                this.sendMessage();
            });
        }
    }

    async sendMessage() {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();

        if (!message) return;

        // Add user message to chat
        this.addMessage(message, 'user');
        messageInput.value = '';

        // Show loading
        this.showLoading();

        try {
            // Get AI response
            const response = await this.getAIResponse(message);
            this.addMessage(response, 'bot');
        } catch (error) {
            console.error('Error getting AI response:', error);
            this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        } finally {
            this.hideLoading();
        }
    }

    addMessage(content, sender) {
        const chatMessages = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = sender === 'bot' ? '<i class="fas fa-robot"></i>' : '<i class="fas fa-user"></i>';

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.innerHTML = `<p>${content}</p>`;

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);

        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async getAIResponse(message) {
        try {
            // Try to get response from backend API first
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            if (response.ok) {
                const data = await response.json();
                return data.response;
            }
        } catch (error) {
            console.log('Backend not available, using fallback responses');
        }

        // Fallback to keyword-based responses
        const responses = this.getResponsesByKeywords(message);
        
        if (responses.length > 0) {
            return responses[Math.floor(Math.random() * responses.length)];
        }

        // Default responses
        const defaultResponses = [
            "That's an interesting question about AI! Let me help you understand this concept better. Could you be more specific about what aspect you'd like to learn about?",
            "I'd be happy to help you with that AI concept! Could you provide more details so I can give you a more targeted explanation?",
            "That's a great question! In the context of Artificial Intelligence, this is an important topic. Let me break it down for you in a way that's easy to understand.",
            "I understand you're asking about AI concepts. This is a fascinating area of study! Could you tell me more about what specific aspect you're curious about?"
        ];

        return defaultResponses[Math.floor(Math.random() * defaultResponses.length)];
    }

    getResponsesByKeywords(message) {
        const lowerMessage = message.toLowerCase();
        const responses = [];

        // AI Definition responses
        if (lowerMessage.includes('what is ai') || lowerMessage.includes('artificial intelligence')) {
            responses.push(`Artificial Intelligence (AI) is the science and engineering of making intelligent machines, especially intelligent computer programs. It enables computers to perform tasks that typically require human intelligence, including learning, reasoning, problem-solving, perception, and understanding language.

AI is relevant to any intellectual task where machines need to make decisions or choose actions based on the current system state. The significance of AI in modern computing includes:

• Universal Application: AI has a wide range of applications across virtually all domains
• Decision Making: Enables automated, intelligent decision-making in complex scenarios  
• Adaptation: Systems can adapt to changing conditions and learn from experience
• Efficiency: Automates tasks that previously required human intervention
• Problem Solving: Tackles complex problems through computational intelligence

AI represents a transformative technology that extends computational capabilities beyond traditional programming to include intelligent behavior and autonomous decision-making.`);
        }

        // Machine Learning responses
        if (lowerMessage.includes('machine learning') || lowerMessage.includes('ml')) {
            responses.push(`Machine Learning is a subset of Artificial Intelligence that focuses on algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience, without being explicitly programmed.

Key concepts in Machine Learning include:

• Supervised Learning: Learning with labeled training data (e.g., classification, regression)
• Unsupervised Learning: Finding patterns in data without labels (e.g., clustering, dimensionality reduction)
• Reinforcement Learning: Learning through interaction with an environment using rewards and penalties
• Deep Learning: Using neural networks with multiple layers to model complex patterns

Machine Learning is widely used in applications like recommendation systems, image recognition, natural language processing, and autonomous vehicles.`);
        }

        // Neural Networks responses
        if (lowerMessage.includes('neural network') || lowerMessage.includes('deep learning')) {
            responses.push(`Neural Networks are computing systems inspired by biological neural networks. They consist of interconnected nodes (neurons) that process information by responding to external inputs and relaying information between each other.

Key components of Neural Networks:

• Input Layer: Receives the initial data
• Hidden Layers: Process the data through weighted connections and activation functions
• Output Layer: Produces the final result
• Weights: Parameters that are adjusted during training
• Activation Functions: Determine whether a neuron should be activated

Deep Learning uses neural networks with many hidden layers to model complex patterns in data. This has led to breakthroughs in computer vision, natural language processing, and many other AI applications.`);
        }

        // Search Algorithms responses
        if (lowerMessage.includes('search algorithm') || lowerMessage.includes('search')) {
            responses.push(`Search Algorithms are fundamental techniques in AI for finding solutions to problems by exploring possible states or paths. They are crucial for problem-solving agents.

Main types of search algorithms:

• Uninformed Search: No additional information about the problem
  - Breadth-First Search (BFS): Explores level by level
  - Depth-First Search (DFS): Explores as deep as possible
  - Uniform Cost Search: Considers path costs

• Informed Search: Uses heuristic information
  - A* Search: Combines actual cost with heuristic estimate
  - Greedy Best-First Search: Uses only heuristic information

These algorithms are used in pathfinding, puzzle solving, game playing, and many other AI applications.`);
        }

        return responses;
    }

    setupQuiz() {
        // Quiz functionality will be implemented here
    }

    async loadQuizData() {
        try {
            // Try to load MCQ data from backend API first
            const response = await fetch('/api/quiz/easy');
            if (response.ok) {
                const data = await response.json();
                this.quizQuestions = data.questions || [];
                console.log('Loaded quiz data from backend API:', this.quizQuestions.length, 'questions');
                return;
            }
        } catch (error) {
            console.log('Backend API not available, trying local files');
        }

        try {
            // Try to load MCQ data from local file
            const response = await fetch('ai_mcq_500plus.json');
            const data = await response.json();
            this.quizQuestions = data.mcqs || [];
            
            if (this.quizQuestions.length === 0) {
                throw new Error('No MCQ data found');
            }
            console.log('Loaded quiz data from local file:', this.quizQuestions.length, 'questions');
        } catch (error) {
            console.error('Error loading MCQ data:', error);
            try {
                // Fallback to Q&A data conversion
                const response = await fetch('ai_qa_dataset.json');
                const data = await response.json();
                this.quizQuestions = this.convertToQuizFormat(data.qa_pairs);
                console.log('Loaded quiz data from Q&A conversion:', this.quizQuestions.length, 'questions');
            } catch (qaError) {
                console.error('Error loading Q&A data:', qaError);
                // Final fallback
                this.quizQuestions = this.getFallbackQuizData();
                console.log('Using fallback quiz data:', this.quizQuestions.length, 'questions');
            }
        }
    }

    convertToQuizFormat(qaPairs) {
        // Convert Q&A pairs to multiple choice questions
        const quizQuestions = [];
        
        qaPairs.forEach((qa, index) => {
            if (index < 20) { // Limit to 20 questions for demo
                const question = {
                    id: qa.id,
                    question: qa.question,
                    correctAnswer: 'A', // Default correct answer
                    options: [
                        qa.answer.substring(0, 100) + '...', // Truncated correct answer
                        this.generateDistractor(qa.category),
                        this.generateDistractor(qa.category),
                        this.generateDistractor(qa.category)
                    ],
                    explanation: qa.answer,
                    category: qa.category,
                    difficulty: this.getDifficulty(qa.category)
                };
                quizQuestions.push(question);
            }
        });
        
        return quizQuestions;
    }

    generateDistractor(category) {
        const distractors = {
            'Introduction to AI': [
                'AI is only useful for simple tasks',
                'AI requires no programming knowledge',
                'AI can only work with text data'
            ],
            'Search Algorithms': [
                'Search algorithms are not important in AI',
                'All search algorithms work the same way',
                'Search algorithms only work with numbers'
            ],
            'Machine Learning': [
                'Machine learning requires no data',
                'All ML algorithms are supervised',
                'Deep learning is not part of ML'
            ]
        };
        
        const categoryDistractors = distractors[category] || [
            'This is not correct',
            'This statement is false',
            'This is inaccurate'
        ];
        
        return categoryDistractors[Math.floor(Math.random() * categoryDistractors.length)];
    }

    getDifficulty(category) {
        const difficultyMap = {
            'Introduction to AI': 'easy',
            'Search Algorithms': 'medium',
            'Machine Learning': 'hard'
        };
        return difficultyMap[category] || 'medium';
    }

    getFallbackQuizData() {
        return [
            {
                id: 1,
                question: "What is Artificial Intelligence?",
                correctAnswer: "A",
                options: [
                    "The science and engineering of making intelligent machines",
                    "A type of computer virus",
                    "A programming language",
                    "A database management system"
                ],
                explanation: "AI is defined as the science and engineering of making intelligent machines, especially intelligent computer programs.",
                category: "Introduction to AI",
                difficulty: "easy"
            },
            {
                id: 2,
                question: "Which search algorithm uses a queue data structure?",
                correctAnswer: "B",
                options: [
                    "Depth-First Search",
                    "Breadth-First Search",
                    "A* Search",
                    "Hill Climbing"
                ],
                explanation: "Breadth-First Search uses a Queue (FIFO - First In First Out) data structure.",
                category: "Search Algorithms",
                difficulty: "medium"
            }
        ];
    }

    async startQuiz(difficulty) {
        this.currentQuiz = difficulty;
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.userAnswers = [];
        
        try {
            // Try to load questions from backend API by difficulty
            const response = await fetch(`/api/quiz/${difficulty}`);
            if (response.ok) {
                const data = await response.json();
                this.quizQuestions = data.questions || [];
                console.log(`Loaded ${this.quizQuestions.length} ${difficulty} questions from API`);
            } else {
                // Fallback to filtering existing questions
                const filteredQuestions = this.quizQuestions.filter(q => q.difficulty === difficulty);
                this.quizQuestions = filteredQuestions.slice(0, 10);
                console.log(`Using ${this.quizQuestions.length} filtered ${difficulty} questions`);
            }
        } catch (error) {
            console.log('API not available, using local questions');
            // Filter questions by difficulty from loaded data
            const filteredQuestions = this.quizQuestions.filter(q => q.difficulty === difficulty);
            this.quizQuestions = filteredQuestions.slice(0, 10);
        }
        
        if (this.quizQuestions.length === 0) {
            alert(`No ${difficulty} questions available. Please try another difficulty level.`);
            this.showQuizWelcome();
            return;
        }
        
        this.showQuizQuestion();
    }

    showQuizQuestion() {
        const quizContainer = document.getElementById('quizContainer');
        const question = this.quizQuestions[this.currentQuestionIndex];
        
        if (!question) {
            this.showQuizResults();
            return;
        }

        // Handle both old and new question formats
        const options = question.options || (question.options ? Object.values(question.options) : []);
        const correctAnswer = question.correct_answer || question.correctAnswer;
        
        const questionHTML = `
            <div class="quiz-question">
                <div class="question-header">
                    <div class="question-number">Question ${this.currentQuestionIndex + 1} of ${this.quizQuestions.length}</div>
                    <div class="question-timer" id="timer">Time: 60s</div>
                </div>
                <div class="question-text">${question.question}</div>
                <div class="question-options">
                    ${options.map((option, index) => `
                        <div class="option" data-option="${String.fromCharCode(65 + index)}" onclick="studBot.selectOption('${String.fromCharCode(65 + index)}')">
                            <div class="option-letter">${String.fromCharCode(65 + index)}</div>
                            <div class="option-text">${option}</div>
                        </div>
                    `).join('')}
                </div>
                <div class="quiz-controls">
                    <div class="quiz-progress">
                        <span>Progress:</span>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${((this.currentQuestionIndex + 1) / this.quizQuestions.length) * 100}%"></div>
                        </div>
                    </div>
                    <div class="quiz-actions">
                        <button class="btn btn-secondary" onclick="studBot.previousQuestion()" ${this.currentQuestionIndex === 0 ? 'disabled' : ''}>Previous</button>
                        <button class="btn btn-primary" onclick="studBot.nextQuestion()" ${this.userAnswers[this.currentQuestionIndex] ? '' : 'disabled'}>Next</button>
                    </div>
                </div>
            </div>
        `;
        
        quizContainer.innerHTML = questionHTML;
        this.startTimer();
    }

    selectOption(option) {
        // Remove previous selection
        const options = document.querySelectorAll('.option');
        options.forEach(opt => opt.classList.remove('selected'));
        
        // Add selection to clicked option
        const selectedOption = document.querySelector(`[data-option="${option}"]`);
        selectedOption.classList.add('selected');
        
        // Store user answer
        this.userAnswers[this.currentQuestionIndex] = option;
        
        // Enable next button
        const nextBtn = document.querySelector('.quiz-actions .btn-primary');
        nextBtn.disabled = false;
    }

    nextQuestion() {
        if (this.currentQuestionIndex < this.quizQuestions.length - 1) {
            this.currentQuestionIndex++;
            this.showQuizQuestion();
        } else {
            this.showQuizResults();
        }
    }

    previousQuestion() {
        if (this.currentQuestionIndex > 0) {
            this.currentQuestionIndex--;
            this.showQuizQuestion();
        }
    }

    startTimer() {
        this.timeLeft = 60;
        this.quizTimer = setInterval(() => {
            this.timeLeft--;
            const timerElement = document.getElementById('timer');
            if (timerElement) {
                timerElement.textContent = `Time: ${this.timeLeft}s`;
            }
            
            if (this.timeLeft <= 0) {
                clearInterval(this.quizTimer);
                this.nextQuestion();
            }
        }, 1000);
    }

    showQuizResults() {
        clearInterval(this.quizTimer);
        
        // Calculate score
        this.score = 0;
        this.quizQuestions.forEach((question, index) => {
            const correctAnswer = question.correct_answer || question.correctAnswer;
            if (this.userAnswers[index] === correctAnswer) {
                this.score++;
            }
        });
        
        const percentage = Math.round((this.score / this.quizQuestions.length) * 100);
        
        const quizContainer = document.getElementById('quizContainer');
        quizContainer.innerHTML = `
            <div class="quiz-results">
                <div class="results-header">
                    <div class="results-icon">
                        <i class="fas fa-trophy"></i>
                    </div>
                    <h3>Quiz Complete!</h3>
                    <p>You scored ${this.score} out of ${this.quizQuestions.length} questions</p>
                </div>
                <div class="results-score">
                    <div class="score-circle">
                        <span class="score-percentage">${percentage}%</span>
                    </div>
                </div>
                <div class="results-message">
                    ${this.getScoreMessage(percentage)}
                </div>
                <div class="results-actions">
                    <button class="btn btn-primary" onclick="studBot.startQuiz('${this.currentQuiz}')">Retake Quiz</button>
                    <button class="btn btn-secondary" onclick="studBot.showQuizWelcome()">Choose Difficulty</button>
                </div>
            </div>
        `;
    }

    getScoreMessage(percentage) {
        if (percentage >= 90) {
            return "Excellent! You have a strong understanding of AI concepts!";
        } else if (percentage >= 70) {
            return "Good job! You're well on your way to mastering AI!";
        } else if (percentage >= 50) {
            return "Not bad! Keep studying to improve your knowledge!";
        } else {
            return "Keep learning! Review the concepts and try again!";
        }
    }

    showQuizWelcome() {
        const quizContainer = document.getElementById('quizContainer');
        quizContainer.innerHTML = `
            <div class="quiz-welcome">
                <div class="quiz-icon">
                    <i class="fas fa-graduation-cap"></i>
                </div>
                <h3>Ready to Test Your AI Knowledge?</h3>
                <p>Choose your difficulty level and start the quiz</p>
                <div class="difficulty-selector">
                    <button class="difficulty-btn" data-level="easy" onclick="studBot.startQuiz('easy')">
                        <i class="fas fa-seedling"></i>
                        Easy
                    </button>
                    <button class="difficulty-btn" data-level="medium" onclick="studBot.startQuiz('medium')">
                        <i class="fas fa-fire"></i>
                        Medium
                    </button>
                    <button class="difficulty-btn" data-level="hard" onclick="studBot.startQuiz('hard')">
                        <i class="fas fa-mountain"></i>
                        Hard
                    </button>
                </div>
            </div>
        `;
    }

    showLoading() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.classList.add('show');
        }
    }

    hideLoading() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.classList.remove('show');
        }
    }
}

// Global functions for HTML onclick events
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function askQuickQuestion(question) {
    const messageInput = document.getElementById('messageInput');
    if (messageInput) {
        messageInput.value = question;
        studBot.sendMessage();
    }
}

function clearChat() {
    const chatMessages = document.getElementById('chatMessages');
    if (chatMessages) {
        chatMessages.innerHTML = `
            <div class="message bot-message">
                <div class="message-avatar">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="message-content">
                    <p>Hello! I'm StudBot, your AI learning companion. I can help you understand Artificial Intelligence concepts, answer your questions, and guide you through your BSc IT studies. What would you like to learn about today?</p>
                </div>
            </div>
        `;
    }
}

// Initialize the application
let studBot;
document.addEventListener('DOMContentLoaded', () => {
    studBot = new StudBot();
});

// Add some additional utility functions
function addParticleEffect() {
    const hero = document.querySelector('.hero');
    if (hero) {
        for (let i = 0; i < 10; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 6 + 's';
            particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
            hero.appendChild(particle);
        }
    }
}

// Add particle effect on load
window.addEventListener('load', addParticleEffect);

// Add scroll effect to navbar
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    }
});
