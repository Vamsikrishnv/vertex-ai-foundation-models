# Stack Overflow Q&A Assistant

> Built an end-to-end ML pipeline to create a Python Q&A assistant using 10,000 real Stack Overflow questions.  
> Learned way more from things breaking than if they'd worked perfectly.

![Project Status](https://img.shields.io/badge/status-complete-success)
![Cost](https://img.shields.io/badge/cost-$0-success)
![Learning](https://img.shields.io/badge/learning-extensive-blue)

---

## What This Does

Ask it Python questions, get answers with code examples and explanations - just like Stack Overflow developers would answer.
```
You: "How do I read a CSV file in pandas?"
Bot: [Gives pandas code, explains each part, shows examples]
```

**But the real value?** Learning how ML pipelines work in the real world - with API deprecations, budget constraints, and content moderation issues.

---

## The Journey (Honest Version)

### What Worked

**Data Pipeline (L2)**
- Extracted 10,000 Python Q&As from BigQuery's public Stack Overflow dataset
- Used SQL JOINs to combine questions with accepted answers
- Filtered for quality (Python tag, post-2020, accepted answers)
- Processed with Pandas: 8,000 training / 2,000 testing
- Formatted as JSONL for model training

**Production Application (L4)**
- Built working Q&A assistant using OpenAI's GPT-4o-mini
- Optimized system prompts for Stack Overflow style
- Interactive CLI interface
- Error handling and logging
- Secure API key management (.env)

### ❌ What Didn't Work (And What I Learned)

**Attempt 1: Google Cloud Vertex AI**
- Problem: text-bison API deprecated mid-project
- Tried: 6 different Gemini model variants
- Result: "Base model not supported" in my region
- Learned: APIs change, real projects adapt

**Attempt 2: OpenAI Fine-tuning (7,200 examples)**
- Problem: Cost $55, budget $3.38
- Result: Exceeded quota
- Learned: Token costs add up FAST

**Attempt 3: OpenAI Fine-tuning (500 examples)**
- Problem: Still cost $4-5
- Result: Over budget
- Learned: Even small datasets can be expensive

**Attempt 4: OpenAI Fine-tuning (100 examples)**
- Problem: Content moderation flagged "unsafe"
- Result: Blocked (Stack Overflow data contains security discussions, looks "sketchy" to AI)
- Learned: OpenAI's moderation is strict with programming data

**Final Decision: Base Model + Prompt Engineering**
- Cost: $0 vs $55
- Time: Immediate vs 60min training
- Performance: Validated as sufficient for use case
- Learned: Simple solutions often beat complex ones

---

## The Tech Stack

| Component | Technology | Why This Choice |
|-----------|-----------|-----------------|
| Data Source | Google BigQuery | Free public Stack Overflow dataset |
| Data Processing | Python, Pandas, sklearn | Industry standard data tools |
| Model | OpenAI GPT-4o-mini | Cost-effective, good performance |
| API Integration | OpenAI API | Reliable, well-documented |
| Security | python-dotenv | Never commit API keys |
| Development | Jupyter Notebooks | Interactive development |

---

## What I Actually Learned

### Technical Skills
- **Data Engineering:** BigQuery SQL, JOINs, filtering 10K+ records
- **Data Processing:** Pandas transformations, train/test splits
- **API Integration:** OpenAI API, error handling, rate limits
- **Security:** Environment variables, .gitignore patterns
- **Prompt Engineering:** System prompts, temperature tuning
- **Version Control:** Git, GitHub, proper .gitignore

### Engineering Skills (The Real Stuff)
- **Debugging:** Spent 3+ hours debugging API deprecation issues
- **Cost Analysis:** Compared $55 vs $4 vs $0 solutions
- **Trade-offs:** Performance vs cost vs time decisions
- **Adaptation:** Pivoted approach 4 times when blocked
- **Documentation:** Kept detailed notes of all attempts
- **Problem-Solving:** Systematic approach when things break

### Real-World Lessons
1. **Things break constantly** - APIs deprecate, services change
2. **Cost matters** - Can't just throw money at problems
3. **Simple often wins** - Base model + prompts worked great
4. **Document failures** - They teach more than successes
5. **Know when to pivot** - After 4 blockers, try something else

---

## Project Structure
```
├── L2_data_exploration.ipynb          # Data extraction from BigQuery
├── L3_automation.ipynb                 # Kubeflow Pipelines (Google Cloud attempt)
├── L3_openai_finetuning.ipynb         # Fine-tuning attempts (4x, all failed)
├── L4_predictions.ipynb                # Working application ✅
├── tune_data_*.jsonl                   # Training data (10K Q&As)
├── .env                                # API keys (gitignored)
├── .gitignore                          # Security
└── README.md                           # You're here
```

---

## How to Run It

### Prerequisites
```bash
- Python 3.8+
- OpenAI API key
- ~$0 cost (uses base model)
```

### Setup
```bash
# Clone and enter directory
git clone <your-repo>
cd llmops-stackoverflow-qa

# Virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install openai pandas python-dotenv jupyter

# Add your API key
echo "OPENAI_API_KEY=your-key-here" > .env
```

### Run
```bash
jupyter notebook L4_predictions.ipynb
# Run all cells, then ask questions!
```

---

## Key Results

### Quantitative
- 10,000 Q&A pairs extracted and processed
- 8,000/2,000 train/test split
- 4 different fine-tuning attempts documented
- $0 final cost (saved $55 through optimization)
- 100% working Q&A assistant

### Qualitative
- Understanding of end-to-end ML pipelines
- Real-world debugging experience
- Cost-benefit analysis skills
- Engineering decision-making under constraints
- Adaptation when plans fail

---

## The Honest Bottom Line

**What I set out to do:** Fine-tune a model on Stack Overflow data

**What actually happened:** Hit 4 different blockers, learned 10x more than if it worked first try

**Final result:** Working Q&A assistant + deep understanding of ML operations

**Would I recommend this project?** Yes - but for the journey, not the destination

**Time invested:** 2 weeks

**Money spent:** $0 (budget was $3.38, used $0)

**Value gained:** Understanding how real ML projects work (messy, with constraints, requiring adaptability)

---

## What's Next

This was a **learning project** to understand LLMOps fundamentals.

**Next applications** will solve real problems:
- Healthcare: Clinical documentation automation
- Manufacturing: Quality control systems
- Dental: Appointment and intake automation

This project taught me the pipeline. Those will apply it where it matters.

---

## Technologies Used

**Languages:** Python, SQL  
**Data:** BigQuery, Pandas, JSONL  
**ML:** OpenAI API, GPT-4o-mini  
**Tools:** Jupyter, Git, python-dotenv  
**Cloud:** Google Cloud Platform (attempted), OpenAI

---

## Lessons for Others

If you're building something similar:

1. **Start simple** - Don't jump to fine-tuning immediately
2. **Budget matters** - Check token costs BEFORE uploading data
3. **Content moderation exists** - Public data (Stack Overflow, Reddit) often gets flagged
4. **Document everything** - Failed attempts teach more than successes
5. **Base models are good** - Prompt engineering often sufficient
6. **APIs change** - text-bison got deprecated mid-project, be ready to adapt

---

## Contact

**Built by:** Krishna 
**Focus:** ML Engineering, Healthcare AI, Manufacturing Automation  
**Learning Style:** Build real things, document everything, learn from failures

---

## License

This is a learning project. Code is MIT licensed. Stack Overflow data is used under their CC BY-SA license.

---

**Status:** Complete   
**Last Updated:** December 2024  
**Biggest Learning:** Real engineering is about solving problems with constraints, not following perfect tutorials.