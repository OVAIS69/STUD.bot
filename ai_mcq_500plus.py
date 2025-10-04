"""
AI Syllabus MCQ Dataset Generator - 100 Questions
20 MCQs per unit covering all major topics
"""

import json
import csv
from datetime import datetime
from typing import List

class MCQGenerator:
    def __init__(self):
        self.mcqs = []
        self.stats = {'easy': 0, 'medium': 0, 'hard': 0}
        
    def add_mcq(self, question, options, correct, explanation, category, difficulty, keywords, unit, topic):
        self.mcqs.append({
            "id": len(self.mcqs) + 1,
            "question": question,
            "options": {"A": options[0], "B": options[1], "C": options[2], "D": options[3]},
            "correct_answer": correct,
            "explanation": explanation,
            "category": category,
            "difficulty": difficulty,
            "keywords": keywords,
            "unit": unit,
            "topic": topic
        })
        self.stats[difficulty] += 1
    
    def export_json(self, filename="ai_mcq_100.json"):
        dataset = {
            "metadata": {
                "total_questions": len(self.mcqs),
                "difficulty_distribution": self.stats,
                "units_covered": ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"],
                "created_at": datetime.now().isoformat()
            },
            "mcqs": self.mcqs
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        return len(self.mcqs)
    
    def export_csv(self, filename="ai_mcq_100.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'question', 'option_A', 'option_B', 
                                                    'option_C', 'option_D', 'correct_answer', 
                                                    'explanation', 'category', 'difficulty', 
                                                    'unit', 'topic'])
            writer.writeheader()
            for mcq in self.mcqs:
                writer.writerow({
                    'id': mcq['id'], 'question': mcq['question'],
                    'option_A': mcq['options']['A'], 'option_B': mcq['options']['B'],
                    'option_C': mcq['options']['C'], 'option_D': mcq['options']['D'],
                    'correct_answer': mcq['correct_answer'], 'explanation': mcq['explanation'],
                    'category': mcq['category'], 'difficulty': mcq['difficulty'],
                    'unit': mcq['unit'], 'topic': mcq['topic']
                })

gen = MCQGenerator()

# ============================================================================
# UNIT 1: INTRODUCTION TO AI (20 MCQs)
# ============================================================================

gen.add_mcq(
    "Who coined the term 'Artificial Intelligence' in 1956?",
    ["Alan Turing", "John McCarthy", "Marvin Minsky", "Herbert Simon"],
    "B",
    "John McCarthy coined 'Artificial Intelligence' at the Dartmouth Conference in 1956.",
    "Introduction", "easy", ["history", "McCarthy"], "Unit 1", "AI Definition"
)

gen.add_mcq(
    "What is Narrow AI also known as?",
    ["Strong AI", "Weak AI", "General AI", "Super AI"],
    "B",
    "Narrow AI is called Weak AI - designed for specific tasks only.",
    "AI Types", "easy", ["Narrow AI", "Weak AI"], "Unit 1", "Types of AI"
)

gen.add_mcq(
    "Which is an example of Narrow AI?",
    ["Human-level intelligence", "Google Translate", "Conscious machines", "General problem solver"],
    "B",
    "Google Translate is Narrow AI performing specific language translation tasks.",
    "AI Types", "easy", ["examples", "applications"], "Unit 1", "Types of AI"
)

gen.add_mcq(
    "General AI (Strong AI) is currently:",
    ["Widely available", "Theoretical and under research", "Used in smartphones", "Deployed in cars"],
    "B",
    "General AI remains theoretical with no practical implementations yet.",
    "AI Types", "medium", ["General AI", "Strong AI"], "Unit 1", "Types of AI"
)

gen.add_mcq(
    "The Turing Test evaluates AI based on:",
    ["Processing speed", "Human-like behavior in conversation", "Memory capacity", "Computational power"],
    "B",
    "Turing Test checks if machine behavior is indistinguishable from humans in text conversation.",
    "AI Approaches", "medium", ["Turing Test", "evaluation"], "Unit 1", "Approaches"
)

gen.add_mcq(
    "Which approach is based on Aristotelian logic?",
    ["Acting Humanly", "Thinking Humanly", "Thinking Rationally", "Acting Rationally"],
    "C",
    "Thinking Rationally (Laws of Thought) is based on Aristotelian logic and formal reasoning.",
    "AI Approaches", "medium", ["logic", "rational thinking"], "Unit 1", "Approaches"
)

gen.add_mcq(
    "A Rational Agent acts to:",
    ["Think like humans", "Achieve best expected outcome", "Display emotions", "Make random choices"],
    "B",
    "Rational agents act to maximize expected performance or utility.",
    "AI Approaches", "medium", ["Rational Agent", "utility"], "Unit 1", "Approaches"
)

gen.add_mcq(
    "Human brains differ from computers by:",
    ["Parallel processing vs sequential", "Slower calculations", "Less memory", "No logic capability"],
    "A",
    "Human brains excel at parallel processing; computers are primarily sequential.",
    "Comparison", "medium", ["brain", "computer"], "Unit 1", "Brain vs Computer"
)

gen.add_mcq(
    "Mathematics contributes what to AI?",
    ["Neural inspiration", "Formal logic and probability", "Language rules", "Cognition models"],
    "B",
    "Mathematics provides formal logic, probability theory, and computational foundations.",
    "Foundations", "medium", ["Mathematics", "logic"], "Unit 1", "Foundations"
)

gen.add_mcq(
    "What caused AI Winters in 1970s-1980s?",
    ["Too much success", "Unfulfilled promises and limited resources", "Excessive funding", "Too many applications"],
    "B",
    "AI Winters resulted from unfulfilled promises, weak computers, and funding cuts.",
    "History", "medium", ["AI Winter", "history"], "Unit 1", "History"
)

gen.add_mcq(
    "What is an AI agent?",
    ["A human operator", "System that perceives and acts", "A database", "A programming language"],
    "B",
    "AI agent perceives environment through sensors and acts via actuators.",
    "Agents", "easy", ["agent", "perception"], "Unit 1", "Agents"
)

gen.add_mcq(
    "The agent cycle is:",
    ["Think only", "Perceive → Think → Act", "Act → Perceive", "Random actions"],
    "B",
    "Agent cycle: Perceive environment → Think/Process → Act → Repeat.",
    "Agents", "easy", ["cycle", "workflow"], "Unit 1", "Agents"
)

gen.add_mcq(
    "In PEAS framework, 'P' stands for:",
    ["Process", "Performance Measure", "Perception", "Planning"],
    "B",
    "PEAS: Performance Measure, Environment, Actuators, Sensors.",
    "Agents", "easy", ["PEAS", "framework"], "Unit 1", "Agents"
)

gen.add_mcq(
    "Simple Reflex Agents operate based on:",
    ["Historical data", "Current percept only", "Future predictions", "Learning"],
    "B",
    "Simple reflex agents use condition-action rules based on current perception only.",
    "Agent Types", "medium", ["simple reflex", "current"], "Unit 1", "Agent Types"
)

gen.add_mcq(
    "Which agent maintains internal state?",
    ["Simple Reflex", "Model-Based Reflex", "Random", "Static"],
    "B",
    "Model-based reflex agents maintain internal state to handle partial observability.",
    "Agent Types", "medium", ["model-based", "state"], "Unit 1", "Agent Types"
)

gen.add_mcq(
    "Learning Agents can:",
    ["Never change", "Improve from experience", "Only use rules", "Work without sensors"],
    "B",
    "Learning agents adapt and improve performance through experience over time.",
    "Agent Types", "easy", ["learning", "adaptation"], "Unit 1", "Agent Types"
)

gen.add_mcq(
    "Chess is which environment type?",
    ["Partially observable", "Fully observable", "Unobservable", "Random"],
    "B",
    "Chess is fully observable - all pieces and positions are visible.",
    "Environments", "easy", ["chess", "observable"], "Unit 1", "Environments"
)

gen.add_mcq(
    "Deterministic environments have:",
    ["Random outcomes", "Predictable outcomes", "No rules", "Uncertainty"],
    "B",
    "Deterministic environments have predictable outcomes from given state and action.",
    "Environments", "easy", ["deterministic", "predictable"], "Unit 1", "Environments"
)

gen.add_mcq(
    "Image classification is:",
    ["Sequential", "Episodic", "Continuous", "Dependent"],
    "B",
    "Image classification is episodic - each image processed independently.",
    "Environments", "medium", ["episodic", "independent"], "Unit 1", "Environments"
)

gen.add_mcq(
    "Dynamic environments are:",
    ["Never change", "Change during agent deliberation", "Always static", "Predictable"],
    "B",
    "Dynamic environments change while agent is thinking/deliberating.",
    "Environments", "easy", ["dynamic", "changing"], "Unit 1", "Environments"
)

# ============================================================================
# UNIT 2: SEARCH ALGORITHMS (20 MCQs)
# ============================================================================

gen.add_mcq(
    "BFS uses which data structure?",
    ["Stack", "Queue", "Tree", "Heap"],
    "B",
    "Breadth-First Search uses Queue (FIFO - First In First Out).",
    "Uninformed Search", "easy", ["BFS", "queue"], "Unit 2", "BFS"
)

gen.add_mcq(
    "DFS uses which data structure?",
    ["Queue", "Stack", "Array", "List"],
    "B",
    "Depth-First Search uses Stack (LIFO - Last In First Out) or recursion.",
    "Uninformed Search", "easy", ["DFS", "stack"], "Unit 2", "DFS"
)

gen.add_mcq(
    "Is BFS optimal for uniform costs?",
    ["Never", "Always", "Sometimes", "Only in trees"],
    "B",
    "BFS is optimal when all step costs are equal (uniform cost).",
    "Uninformed Search", "medium", ["BFS", "optimality"], "Unit 2", "BFS"
)

gen.add_mcq(
    "Which uses more memory?",
    ["BFS", "DFS", "Both equal", "Neither"],
    "A",
    "BFS uses more memory O(b^d) vs DFS O(bd) as it stores all level nodes.",
    "Uninformed Search", "medium", ["memory", "complexity"], "Unit 2", "Comparison"
)

gen.add_mcq(
    "Uniform Cost Search expands nodes by:",
    ["Depth", "Breadth", "Lowest path cost", "Random"],
    "C",
    "UCS expands nodes in order of lowest cumulative path cost g(n).",
    "Uninformed Search", "medium", ["UCS", "cost"], "Unit 2", "UCS"
)

gen.add_mcq(
    "Depth-Limited Search addresses which DFS problem?",
    ["High memory use", "Infinite paths", "Slow execution", "Poor optimality"],
    "B",
    "Depth-Limited Search prevents infinite path exploration by imposing depth limit.",
    "Uninformed Search", "medium", ["DLS", "depth limit"], "Unit 2", "DLS"
)

gen.add_mcq(
    "IDDFS combines advantages of:",
    ["BFS and UCS", "BFS and DFS", "DFS and UCS", "Only DFS"],
    "B",
    "IDDFS combines BFS completeness/optimality with DFS memory efficiency.",
    "Uninformed Search", "medium", ["IDDFS", "combination"], "Unit 2", "IDDFS"
)

gen.add_mcq(
    "TSP aims to find:",
    ["Longest route", "Shortest route visiting all cities once", "Any valid route", "Fastest algorithm"],
    "B",
    "Traveling Salesman Problem finds shortest route visiting all cities exactly once and returning to origin.",
    "Optimization", "easy", ["TSP", "shortest route"], "Unit 2", "TSP"
)

gen.add_mcq(
    "A* algorithm evaluation function is:",
    ["f(n) = g(n)", "f(n) = h(n)", "f(n) = g(n) + h(n)", "f(n) = g(n) - h(n)"],
    "C",
    "A* uses f(n) = g(n) + h(n) where g is actual cost and h is heuristic estimate.",
    "Informed Search", "medium", ["A*", "formula"], "Unit 2", "A* Search"
)

gen.add_mcq(
    "In A*, g(n) represents:",
    ["Heuristic estimate", "Actual cost from start to n", "Total estimated cost", "Goal distance"],
    "B",
    "g(n) is the actual path cost from start node to current node n.",
    "Informed Search", "medium", ["A*", "g(n)"], "Unit 2", "A* Search"
)

gen.add_mcq(
    "In A*, h(n) represents:",
    ["Actual cost", "Heuristic estimate from n to goal", "Total cost", "Path length"],
    "B",
    "h(n) is the heuristic estimate of remaining cost from node n to goal.",
    "Informed Search", "medium", ["A*", "h(n)"], "Unit 2", "A* Search"
)

gen.add_mcq(
    "Greedy Best-First Search uses:",
    ["f(n) = g(n)", "f(n) = h(n) only", "f(n) = g(n) + h(n)", "f(n) = g(n) * h(n)"],
    "B",
    "Greedy Best-First uses only heuristic h(n) to select nodes that appear closest to goal.",
    "Informed Search", "medium", ["Greedy", "heuristic"], "Unit 2", "Greedy Search"
)

gen.add_mcq(
    "A* is optimal when heuristic is:",
    ["Overestimating", "Admissible (never overestimates)", "Random", "Inconsistent"],
    "B",
    "A* guarantees optimal solution when heuristic is admissible (never overestimates actual cost).",
    "Informed Search", "hard", ["A*", "admissible"], "Unit 2", "A* Search"
)

gen.add_mcq(
    "Hill Climbing is a:",
    ["Global search", "Local search", "Complete search", "Optimal search"],
    "B",
    "Hill Climbing is local search moving to better neighboring states iteratively.",
    "Optimization", "easy", ["Hill Climbing", "local"], "Unit 2", "Hill Climbing"
)

gen.add_mcq(
    "Hill Climbing can get stuck at:",
    ["Global maximum", "Local optima", "Starting point", "Goal state"],
    "B",
    "Hill Climbing gets stuck at local optima, missing global optimum.",
    "Optimization", "medium", ["Hill Climbing", "local optima"], "Unit 2", "Hill Climbing"
)

gen.add_mcq(
    "Genetic Algorithms are inspired by:",
    ["Physics", "Natural evolution", "Economics", "Psychology"],
    "B",
    "Genetic Algorithms mimic biological evolution with selection, crossover, and mutation.",
    "Optimization", "easy", ["GA", "evolution"], "Unit 2", "Genetic Algorithm"
)

gen.add_mcq(
    "In GA, crossover operator:",
    ["Removes individuals", "Combines parent genes", "Mutates randomly", "Selects fitness"],
    "B",
    "Crossover combines genetic material from two parents to create offspring.",
    "Optimization", "medium", ["GA", "crossover"], "Unit 2", "Genetic Algorithm"
)

gen.add_mcq(
    "Bidirectional Search searches from:",
    ["Start only", "Goal only", "Both start and goal simultaneously", "Random points"],
    "C",
    "Bidirectional Search runs two simultaneous searches from start and goal, meeting in middle.",
    "Search Algorithms", "medium", ["Bidirectional", "simultaneous"], "Unit 2", "Bidirectional"
)

gen.add_mcq(
    "Simulated Annealing is inspired by:",
    ["Evolution", "Metallurgy annealing process", "Economics", "Psychology"],
    "B",
    "Simulated Annealing mimics metallurgical annealing - heating and slow cooling process.",
    "Optimization", "medium", ["Simulated Annealing", "metallurgy"], "Unit 2", "Simulated Annealing"
)

gen.add_mcq(
    "Simulated Annealing accepts worse solutions:",
    ["Never", "With decreasing probability over time", "Always", "Randomly"],
    "B",
    "SA probabilistically accepts worse solutions early (high temperature) to escape local optima, decreasing over time.",
    "Optimization", "hard", ["SA", "probability"], "Unit 2", "Simulated Annealing"
)

# ============================================================================
# UNIT 3: ADVERSARIAL SEARCH & KNOWLEDGE (20 MCQs)
# ============================================================================

gen.add_mcq(
    "Minimax algorithm is used in:",
    ["Single-agent problems", "Two-player zero-sum games", "Optimization", "Classification"],
    "B",
    "Minimax is for two-player zero-sum games where one player's gain equals opponent's loss.",
    "Adversarial Search", "easy", ["Minimax", "games"], "Unit 3", "Minimax"
)

gen.add_mcq(
    "In Minimax, MAX player tries to:",
    ["Minimize score", "Maximize score", "Random moves", "Avoid decisions"],
    "B",
    "MAX player attempts to maximize game score/utility.",
    "Adversarial Search", "easy", ["Minimax", "MAX"], "Unit 3", "Minimax"
)

gen.add_mcq(
    "In Minimax, MIN player tries to:",
    ["Maximize score", "Minimize score", "Help MAX", "Random moves"],
    "B",
    "MIN player attempts to minimize score, representing opponent.",
    "Adversarial Search", "easy", ["Minimax", "MIN"], "Unit 3", "Minimax"
)

gen.add_mcq(
    "Alpha-Beta Pruning improves:",
    ["Solution quality", "Minimax efficiency by eliminating branches", "Heuristic accuracy", "Memory usage"],
    "B",
    "Alpha-Beta Pruning reduces Minimax computational cost by pruning irrelevant branches.",
    "Adversarial Search", "medium", ["Alpha-Beta", "pruning"], "Unit 3", "Alpha-Beta"
)

gen.add_mcq(
    "In Alpha-Beta Pruning, Alpha represents:",
    ["Upper bound", "Lower bound (best for MAX)", "Random value", "Goal state"],
    "B",
    "Alpha is lower bound - best value MAX can guarantee so far.",
    "Adversarial Search", "hard", ["Alpha-Beta", "alpha"], "Unit 3", "Alpha-Beta"
)

gen.add_mcq(
    "In Alpha-Beta Pruning, Beta represents:",
    ["Lower bound", "Upper bound (best for MIN)", "Initial value", "Final value"],
    "B",
    "Beta is upper bound - best value MIN can guarantee so far.",
    "Adversarial Search", "hard", ["Alpha-Beta", "beta"], "Unit 3", "Alpha-Beta"
)

gen.add_mcq(
    "Pruning occurs when:",
    ["Alpha < Beta", "Alpha ≥ Beta", "Alpha = 0", "Beta = 0"],
    "B",
    "Branch is pruned when Alpha ≥ Beta, as it won't affect final decision.",
    "Adversarial Search", "hard", ["Alpha-Beta", "condition"], "Unit 3", "Alpha-Beta"
)

gen.add_mcq(
    "Stochastic games involve:",
    ["Perfect prediction", "Probabilistic outcomes", "No uncertainty", "Single player"],
    "B",
    "Stochastic games have probabilistic/random elements affecting outcomes.",
    "Adversarial Search", "medium", ["Stochastic", "probability"], "Unit 3", "Game Types"
)

gen.add_mcq(
    "Partially Observable Games have:",
    ["Complete information", "Hidden information/incomplete state", "Perfect visibility", "No uncertainty"],
    "B",
    "Partially observable games involve hidden information like opponent's cards in poker.",
    "Adversarial Search", "medium", ["Partial observability", "hidden"], "Unit 3", "Game Types"
)

gen.add_mcq(
    "Knowledge-Based Agents use:",
    ["Random actions", "Stored knowledge for decisions", "No memory", "Only reflexes"],
    "B",
    "Knowledge-based agents use stored knowledge base to make informed decisions.",
    "Knowledge", "easy", ["KB agents", "knowledge"], "Unit 3", "KB Agents"
)

gen.add_mcq(
    "Main components of KB agents are:",
    ["Sensors only", "Knowledge Base and Inference Engine", "Actuators only", "Memory only"],
    "B",
    "KB agents have Knowledge Base (facts/rules) and Inference Engine (reasoning).",
    "Knowledge", "medium", ["KB components", "inference"], "Unit 3", "KB Agents"
)

gen.add_mcq(
    "TELL operation in KB agents:",
    ["Queries knowledge", "Adds new information to KB", "Deletes facts", "Executes actions"],
    "B",
    "TELL operation informs/adds new knowledge to the Knowledge Base.",
    "Knowledge", "medium", ["TELL", "operations"], "Unit 3", "KB Agents"
)

gen.add_mcq(
    "ASK operation in KB agents:",
    ["Adds knowledge", "Queries KB for information", "Deletes data", "Performs actions"],
    "B",
    "ASK operation queries Knowledge Base to retrieve information for decisions.",
    "Knowledge", "medium", ["ASK", "operations"], "Unit 3", "KB Agents"
)

gen.add_mcq(
    "Propositional Logic deals with:",
    ["Objects and relations", "True/False propositions", "Probabilities", "Fuzzy values"],
    "B",
    "Propositional Logic uses Boolean true/false statements and logical connectives.",
    "Logic", "easy", ["Propositional", "Boolean"], "Unit 3", "Logic Types"
)

gen.add_mcq(
    "Fuzzy Logic uses:",
    ["Only true/false", "Degrees of truth (0 to 1)", "Integers only", "No truth values"],
    "B",
    "Fuzzy Logic handles partial truth with values between 0 and 1.",
    "Logic", "medium", ["Fuzzy", "degrees"], "Unit 3", "Logic Types"
)

gen.add_mcq(
    "Modal Logic reasons about:",
    ["Certainty only", "Necessity and possibility", "Numbers", "Images"],
    "B",
    "Modal Logic handles necessity (must be true) and possibility (might be true).",
    "Logic", "hard", ["Modal", "necessity"], "Unit 3", "Logic Types"
)

gen.add_mcq(
    "Temporal Logic deals with:",
    ["Space", "Time-based statements", "Probabilities", "Objects"],
    "B",
    "Temporal Logic handles time-dependent statements like 'eventually' and 'always'.",
    "Logic", "medium", ["Temporal", "time"], "Unit 3", "Logic Types"
)

gen.add_mcq(
    "Bayesian Logic uses:",
    ["Only certainty", "Probabilistic reasoning", "Binary values", "No math"],
    "B",
    "Bayesian Logic applies probability theory for reasoning under uncertainty.",
    "Logic", "medium", ["Bayesian", "probability"], "Unit 3", "Logic Types"
)

gen.add_mcq(
    "Probabilistic reasoning is needed because:",
    ["All data is complete", "Real-world involves uncertainty", "Perfect knowledge exists", "No decisions required"],
    "B",
    "Real-world data is incomplete, noisy, and uncertain, requiring probabilistic methods.",
    "Probability", "easy", ["uncertainty", "probability"], "Unit 3", "Probabilistic Reasoning"
)

gen.add_mcq(
    "Bayes' Theorem is used to:",
    ["Add numbers", "Update beliefs with new evidence", "Remove uncertainty", "Generate data"],
    "B",
    "Bayes' Theorem updates probability beliefs when new evidence is observed.",
    "Probability", "medium", ["Bayes", "update"], "Unit 3", "Probabilistic Reasoning"
)

# ============================================================================
# UNIT 4: FIRST-ORDER LOGIC (20 MCQs)
# ============================================================================

gen.add_mcq(
    "First-Order Logic is also called:",
    ["Boolean Logic", "Predicate Logic", "Temporal Logic", "Modal Logic"],
    "B",
    "First-Order Logic (FOL) is also known as Predicate Logic or First-Order Predicate Calculus.",
    "FOL", "easy", ["FOL", "Predicate"], "Unit 4", "FOL Basics"
)

gen.add_mcq(
    "FOL is more expressive than Propositional Logic because it includes:",
    ["Only true/false", "Objects, relations, and quantifiers", "No variables", "Simpler syntax"],
    "B",
    "FOL adds objects, relations, functions, and quantifiers beyond propositional true/false.",
    "FOL", "medium", ["expressiveness", "objects"], "Unit 4", "FOL Basics"
)

gen.add_mcq(
    "Constants in FOL represent:",
    ["Variables", "Specific objects", "Relations", "Functions"],
    "B",
    "Constants represent specific objects like John, 5, Mumbai.",
    "FOL", "easy", ["constants", "objects"], "Unit 4", "FOL Syntax"
)

gen.add_mcq(
    "Variables in FOL are represented by:",
    ["Capital letters", "Lowercase letters like x, y, z", "Numbers", "Symbols"],
    "B",
    "Variables are typically lowercase letters (x, y, z) representing arbitrary objects.",
    "FOL", "easy", ["variables", "notation"], "Unit 4", "FOL Syntax"
)

gen.add_mcq(
    "Predicates in FOL express:",
    ["Objects", "Properties or relations", "Actions", "Constants"],
    "B",
    "Predicates express properties (Red(x)) or relations (Brother(x,y)).",
    "FOL", "easy", ["predicates", "relations"], "Unit 4", "FOL Syntax"
)

gen.add_mcq(
    "Universal Quantifier (∀) means:",
    ["There exists", "For all", "Sometimes", "Never"],
    "B",
    "∀ (universal quantifier) means 'for all' or 'for every' instance.",
    "FOL", "easy", ["universal", "quantifier"], "Unit 4", "Quantifiers"
)

gen.add_mcq(
    "Existential Quantifier (∃) means:",
    ["For all", "There exists at least one", "Never", "Always"],
    "B",
    "∃ (existential quantifier) means 'there exists' or 'for some' instance.",
    "FOL", "easy", ["existential", "quantifier"], "Unit 4", "Quantifiers"
)

gen.add_mcq(
    "'All humans are mortal' in FOL is:",
    ["∃x Human(x)", "∀x (Human(x) → Mortal(x))", "∀x Mortal(x)", "Human → Mortal"],
    "B",
    "Universal quantifier with implication: For all x, if x is human then x is mortal.",
    "FOL", "medium", ["universal", "example"], "Unit 4", "Quantifiers"
)

gen.add_mcq(
    "'Some students are intelligent' in FOL is:",
    ["∀x Intelligent(x)", "∃x (Student(x) ∧ Intelligent(x))", "Student → Intelligent", "∀x Student(x)"],
    "B",
    "Existential quantifier with conjunction: There exists x where x is student AND intelligent.",
    "FOL", "medium", ["existential", "example"], "Unit 4", "Quantifiers"
)

gen.add_mcq(
    "Universal quantifier typically uses which connective?",
    ["AND (∧)", "Implication (→)", "OR (∨)", "NOT (¬)"],
    "B",
    "Universal quantifier ∀ typically uses implication →: ∀x (P(x) → Q(x)).",
    "FOL", "medium", ["universal", "implication"], "Unit 4", "Quantifiers"
)

gen.add_mcq(
    "Existential quantifier typically uses which connective?",
    ["Implication (→)", "Conjunction (∧)", "Equivalence (↔)", "NOT (¬)"],
    "B",
    "Existential quantifier ∃ typically uses conjunction ∧: ∃x (P(x) ∧ Q(x)).",
    "FOL", "medium", ["existential", "conjunction"], "Unit 4", "Quantifiers"
)

gen.add_mcq(
    "Unification is the process of:",
    ["Dividing expressions", "Making two expressions identical via substitutions", "Deleting variables", "Random assignment"],
    "B",
    "Unification finds substitutions to make two logical expressions identical.",
    "FOL", "medium", ["unification", "substitution"], "Unit 4", "Unification"
)

gen.add_mcq(
    "Most General Unifier (MGU) is:",
    ["Most complex substitution", "Simplest substitution achieving unification", "Random substitution", "No substitution"],
    "B",
    "MGU is the simplest/most general substitution set that unifies expressions.",
    "FOL", "hard", ["MGU", "substitution"], "Unit 4", "Unification"
)

gen.add_mcq(
    "For successful unification, predicate names must:",
    ["Be different", "Match exactly", "Be variables", "Not matter"],
    "B",
    "Unification requires matching predicate names: Loves(x,y) cannot unify with Hates(A,B).",
    "FOL", "medium", ["unification", "conditions"], "Unit 4", "Unification"
)