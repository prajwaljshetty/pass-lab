# BruteBeetle 🪲

<div align="center">

**Every combination. Every possibility.**

A recursive brute-force password search engine that systematically generates and tests character combinations until it finds a match.

*Part of [pass-lab](https://github.com/prajwaljshetty/pass-lab) — exploring exhaustive search, recursive generation, hash verification, and the computational complexity of password searching.*

</div>

---

## Contents

- [How It Works](#-how-it-works)
- [Demonstration](#-demonstration)
- [Algorithm & Complexity](#-algorithm--complexity)
- [Implementation](#️-implementation)
- [Getting Started](#-getting-started)
- [Limitations](#️-limitations)

---

## ⚙️ How It Works

BruteBeetle recursively constructs candidate passwords character by character, verifying each complete candidate against a stored SHA-256 hash. When a match is found, a custom exception immediately halts the search.

**Execution flow**

1. Initialize the character set and target length.
2. Recursively generate candidate combinations.
3. Verify each candidate against the stored hash.
4. Track attempts and display search progress.
5. Stop as soon as a match is found.
6. Reveal the recovered password with a terminal animation.

---

## 🧪 Demonstration

**Search progress** — the number of attempted combinations and the percentage of the search space explored.

<p align="center">
  <img src="./images/image1.png" width="80%" style="border-radius: 12px;" alt="BruteBeetle search initialization" />
  <br/><br/>
  <img src="./images/image2.png" width="80%" style="border-radius: 12px;" alt="BruteBeetle search progress" />
</p>

**Password discovery** — once a match is found, BruteBeetle progressively reveals the recovered password.

<p align="center">
  <img src="./images/image3.png" width="80%" style="border-radius: 12px;" alt="BruteBeetle password reveal animation" />
  <br/><br/>
  <img src="./images/image4.png" width="80%" style="border-radius: 12px;" alt="BruteBeetle successful password discovery" />
</p>

---

## 🧮 Algorithm & Complexity

Let \(n\) be the number of available characters and \(L\) the target password length.

**Search space:**

\[
S = n^L
\]

| Measure | Complexity | Explanation |
|---|---|---|
| Time | \(O(n^L)\) | Worst case: every combination must be generated and verified. |
| Auxiliary space | \(O(L)\) | The recursive call stack grows with password length, excluding fixed storage like the character set. |

---

## 🛠️ Implementation

| Component | Responsibility |
|---|---|
| `BruteBeetle` | Controls recursive candidate generation and search execution. |
| `PasswordVault` | Stores the password hash and verifies candidates. |
| `PasswordFound` | Signals a successful match and halts recursion. |
| `show_progress()` | Displays search progress and attempt statistics. |
| `print_success()` | Animates the recovered password, character by character. |

---

## 🚀 Getting Started

**Requirements**

- Python 3.9+
- No external dependencies.

**Clone and run**

```bash
git clone https://github.com/prajwaljshetty/pass-lab.git
cd pass-lab/brute_force

python BruteBeetle.py
```

The demonstration password, character set, and target length are configured in the source code.

---

## ⚠️ Limitations

- Exhaustive search becomes exponentially more expensive as password length and character-set size grow.
- The current implementation only searches passwords of a fixed, specified length.
- SHA-256 is used for demonstration purposes; production password storage should use a dedicated password-hashing algorithm such as Argon2id.
- Intended for controlled experiments and authorized security testing only.

---

<div align="center">

**Objective:** Make exhaustive search tangible — observe how the search space grows, and explore, hands-on, the computational limits of brute-force techniques.

*One character at a time. One combination at a time. Until a match is found.*

Part of [pass-lab](https://github.com/prajwaljshetty/pass-lab) 🔐

</div>
