<div align="center">

# BruteBeetle 🪲

**Every combination. Every possibility.**

A recursive brute-force password search engine that systematically generates and tests character combinations until it finds a match.

Part of [pass-lab](https://github.com/prajwaljshetty/pass-lab) — exploring exhaustive search, recursive generation, hash verification, and the computational complexity of password searching.

</div>

<br />

## Contents

- [How It Works](#how-it-works)
- [Demonstration](#demonstration)
- [Algorithm & Complexity](#algorithm--complexity)
- [Implementation](#implementation)
- [Getting Started](#getting-started)
- [Limitations](#limitations)

<br /><br />

## How It Works

BruteBeetle recursively constructs candidate passwords character by character, verifying each complete candidate against a stored SHA-256 hash. When a match is found, a custom exception immediately halts the search.

1. Initialize the character set and target length
2. Recursively generate candidate combinations
3. Verify each candidate against the stored hash
4. Track attempts and display search progress
5. Stop as soon as a match is found
6. Reveal the recovered password with a terminal animation

<br /><br />

## Demonstration

**Search progress**
The number of attempted combinations and the percentage of the search space explored.

<p align="center">
  <img src="./images/image1.png" width="85%" style="border-radius: 12px;" alt="BruteBeetle search initialization" />
</p>
<p align="center">
  <img src="./images/image2.png" width="85%" style="border-radius: 12px;" alt="BruteBeetle search progress" />
</p>

**Password discovery**
Once a match is found, BruteBeetle progressively reveals the recovered password.

<p align="center">
  <img src="./images/image3.png" width="85%" style="border-radius: 12px;" alt="BruteBeetle password reveal
