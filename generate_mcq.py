"""
Generate MCQ data from Q&A dataset
Converts the comprehensive Q&A data into multiple choice questions
"""

import json
import random
from datetime import datetime

def generate_mcq_from_qa(qa_pairs, num_questions=50):
    """Generate MCQ questions from Q&A pairs"""
    mcqs = []
    
    # Sample questions to convert
    sample_questions = random.sample(qa_pairs, min(num_questions, len(qa_pairs)))
    
    for i, qa in enumerate(sample_questions):
        # Extract key concepts from the answer
        answer_text = qa['answer']
        question_text = qa['question']
        
        # Generate distractors based on category
        distractors = generate_distractors(qa['category'])
        
        # Create correct answer (truncated)
        correct_answer = answer_text[:150] + "..." if len(answer_text) > 150 else answer_text
        
        # Shuffle options
        options = [correct_answer] + distractors[:3]
        random.shuffle(options)
        
        # Find correct answer position
        correct_index = options.index(correct_answer)
        correct_letter = chr(65 + correct_index)  # A, B, C, D
        
        mcq = {
            "id": i + 1,
            "question": question_text,
            "options": {
                "A": options[0],
                "B": options[1],
                "C": options[2],
                "D": options[3]
            },
            "correct_answer": correct_letter,
            "explanation": answer_text,
            "category": qa['category'],
            "difficulty": get_difficulty(qa['category']),
            "keywords": qa.get('keywords', []),
            "unit": get_unit(qa['category']),
            "topic": qa['category']
        }
        
        mcqs.append(mcq)
    
    return mcqs

def generate_distractors(category):
    """Generate plausible distractors based on category"""
    distractors_by_category = {
        "Introduction to AI": [
            "AI is only useful for simple computational tasks",
            "Artificial Intelligence requires no programming knowledge",
            "AI can only work with numerical data",
            "Machine learning is not part of AI",
            "AI systems cannot learn from experience"
        ],
        "Search Algorithms": [
            "Search algorithms are not important in AI",
            "All search algorithms work identically",
            "BFS and DFS are the same algorithm",
            "Search algorithms only work with trees",
            "Heuristic search is always faster than uninformed search"
        ],
        "Machine Learning": [
            "Machine learning requires no training data",
            "All ML algorithms are supervised learning",
            "Deep learning is not part of machine learning",
            "Neural networks cannot learn complex patterns",
            "ML algorithms always give perfect results"
        ],
        "Neural Networks": [
            "Neural networks are only used for classification",
            "All neural networks have the same architecture",
            "Neural networks cannot process sequential data",
            "Deep learning uses only one hidden layer",
            "Neural networks don't need training"
        ],
        "Knowledge Representation": [
            "Knowledge representation is not important in AI",
            "All knowledge can be represented as rules",
            "Logic is the only way to represent knowledge",
            "Knowledge bases don't need updating",
            "Inference is not possible with knowledge representation"
        ],
        "Planning": [
            "Planning is only used in robotics",
            "All planning problems are simple",
            "Planning doesn't require search algorithms",
            "HTN planning is the same as classical planning",
            "Planning cannot handle uncertainty"
        ]
    }
    
    # Get distractors for the category or use general ones
    distractors = distractors_by_category.get(category, [
        "This statement is incorrect",
        "This is not accurate",
        "This is false",
        "This is not true"
    ])
    
    # Return random selection of distractors
    return random.sample(distractors, min(3, len(distractors)))

def get_difficulty(category):
    """Assign difficulty based on category"""
    difficulty_map = {
        "Introduction to AI": "easy",
        "Foundations of AI": "easy",
        "History of AI": "easy",
        "Search Algorithms": "medium",
        "Uninformed Search": "medium",
        "Informed Search": "medium",
        "Optimization Problems": "hard",
        "Optimization Algorithms": "hard",
        "Adversarial Search": "hard",
        "Knowledge Representation": "medium",
        "Logic and Reasoning": "medium",
        "Probabilistic Reasoning": "hard",
        "First Order Logic": "hard",
        "Inference Methods": "hard",
        "Planning": "hard",
        "Generative AI": "medium"
    }
    return difficulty_map.get(category, "medium")

def get_unit(category):
    """Assign unit based on category"""
    unit_map = {
        "Introduction to AI": "Unit 1",
        "Foundations of AI": "Unit 1",
        "History of AI": "Unit 1",
        "AI Environments": "Unit 1",
        "Problem Solving": "Unit 2",
        "Search Algorithms": "Unit 2",
        "Uninformed Search": "Unit 2",
        "Informed Search": "Unit 2",
        "Optimization Problems": "Unit 2",
        "Optimization Algorithms": "Unit 2",
        "Adversarial Search": "Unit 3",
        "Knowledge Representation": "Unit 3",
        "Logic and Reasoning": "Unit 3",
        "Probabilistic Reasoning": "Unit 3",
        "First Order Logic": "Unit 4",
        "Inference Methods": "Unit 4",
        "Planning": "Unit 5",
        "Generative AI": "Unit 5"
    }
    return unit_map.get(category, "Unit 1")

def main():
    """Main function to generate MCQ dataset"""
    print("Generating MCQ dataset from Q&A data...")
    
    # Load Q&A data
    try:
        with open('ai_qa_dataset.json', 'r', encoding='utf-8') as f:
            qa_data = json.load(f)
        qa_pairs = qa_data.get('qa_pairs', [])
        print(f"Loaded {len(qa_pairs)} Q&A pairs")
    except FileNotFoundError:
        print("ai_qa_dataset.json not found!")
        return
    
    # Generate MCQs
    mcqs = generate_mcq_from_qa(qa_pairs, 100)
    
    # Create dataset structure
    dataset = {
        "metadata": {
            "total_questions": len(mcqs),
            "difficulty_distribution": {
                "easy": len([m for m in mcqs if m['difficulty'] == 'easy']),
                "medium": len([m for m in mcqs if m['difficulty'] == 'medium']),
                "hard": len([m for m in mcqs if m['difficulty'] == 'hard'])
            },
            "units_covered": list(set([m['unit'] for m in mcqs])),
            "categories_covered": list(set([m['category'] for m in mcqs])),
            "created_at": datetime.now().isoformat()
        },
        "mcqs": mcqs
    }
    
    # Save to JSON file
    with open('ai_mcq_500plus.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(mcqs)} MCQ questions")
    print(f"Difficulty distribution:")
    print(f"   - Easy: {dataset['metadata']['difficulty_distribution']['easy']}")
    print(f"   - Medium: {dataset['metadata']['difficulty_distribution']['medium']}")
    print(f"   - Hard: {dataset['metadata']['difficulty_distribution']['hard']}")
    print(f"Saved to ai_mcq_500plus.json")
    
    # Also create a smaller sample for testing
    sample_mcqs = random.sample(mcqs, min(20, len(mcqs)))
    sample_dataset = {
        "metadata": {
            "total_questions": len(sample_mcqs),
            "description": "Sample MCQ dataset for testing",
            "created_at": datetime.now().isoformat()
        },
        "mcqs": sample_mcqs
    }
    
    with open('ai_mcq_sample.json', 'w', encoding='utf-8') as f:
        json.dump(sample_dataset, f, indent=2, ensure_ascii=False)
    
    print(f"Created sample dataset with {len(sample_mcqs)} questions (ai_mcq_sample.json)")

if __name__ == "__main__":
    main()
