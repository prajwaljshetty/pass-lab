# pass-lab 🔐

*Understanding passwords. Exploring the techniques behind breaking them.*

Passwords are everywhere. But how secure are they, really?

**pass-lab** is a hands-on security experimentation lab focused on understanding password security, exploring password-cracking techniques, and implementing the algorithms behind them — one experiment at a time.

From exhaustive brute-force searches to dictionary-based attacks, each method explores a different approach to password discovery, its underlying algorithm, computational cost, and limitations.

### 🧪 The Lab

| Experiment | What's happening |
|---|---|
| [`brute_force/`](./brute_force/) | **BruteBeetle** — An exhaustive password search engine that recursively generates and verifies character combinations. |
| `dictionary/` | Exploring wordlist-based password guessing. |
| `hybrid/` | Combining dictionary words with additional character variations. |
| `mask/` | Exploring pattern-based candidate generation. |
| `rule_based/` | Applying transformation rules to password candidates. |

### ⚙️ The Method

**Understand → Implement → Experiment → Measure → Improve**

Every technique is an opportunity to explore the algorithms behind it, understand its computational complexity, and observe how different approaches behave under controlled conditions.

*Every password has a search space. Every search space has a story.*
