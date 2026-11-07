import hashlib
import os
import string
import time

PASSWORD = "prajwal"

class Color:
    PRIMARY = "\033[38;5;208m"
    GREEN = "\033[38;5;46m"
    RED = "\033[38;5;196m"
    YELLOW = "\033[38;5;226m"
    BLUE = "\033[38;5;39m"
    PINK = "\033[38;5;213m"
    PURPLE = "\033[38;5;141m"
    WHITE = "\033[97m"
    CYAN = "\033[38;5;51m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

class PasswordVault:
    """
    Holds only a hash of the real password, never the password itself.

    This models how a real login system works: VOID can ask "does this
    guess match?" and get back True/False, but it has no way to read
    the actual password out of the vault.
    """

    def __init__(self, password):
        self._hash = self._hash_of(password)

    @staticmethod
    def _hash_of(value):
        return hashlib.sha256(value.encode()).hexdigest()

    def verify(self, guess):
        """Check whether a guess matches the stored password hash."""
        return self._hash_of(guess) == self._hash

class PasswordFound(Exception):
    """
    Raised when the correct password is found.
    Used purely as a control-flow signal to unwind the entire
    recursive call stack instantly, instead of letting every
    pending loop/recursion continue after a match is found.
    """

    def __init__(self, password):
        super().__init__(password)
        self.password = password

class BruteBeetle:
    """
    VOID - Variable-Order Identification and Discovery.

    Crawls through every possible combination of characters, in order,
    for a fixed-length password until a match is found.
    """
    def __init__(self, vault, characters=None):
        self.vault = vault
        self.characters = characters or (
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits
            + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        )
        self.attempts = 0

    def crack(self, length):
        """Start the brute-force search for a password of the given length."""
        self.clear_screen()
        self.attempts = 0

        try:
            self._generate(current="", length=length)
        except PasswordFound as found:
            self.print_success(password=found.password, length=length)

    def _generate(self, current, length):
        """
        Recursively build up guesses character by character.
        Once a guess reaches the target length, ask the vault whether
        it matches; if correct, raise PasswordFound to stop the search.
        """
        if len(current) == length:
            self.attempts += 1
            self.show_progress(length)

            if self.vault.verify(current):
                raise PasswordFound(current)
            return

        for character in self.characters:
            self._generate(current + character, length)

    def clear_screen(self):
        """Clear the terminal (cross-platform)."""
        os.system("cls" if os.name == "nt" else "clear")

    def show_progress(self, length, bar_width=30):
        """Print what fraction of the total search space has been tried."""
        total_combinations = len(self.characters) ** length
        percentage = (self.attempts / total_combinations) * 100

        filled = int(bar_width * percentage / 100)
        bar = "█" * filled + "░" * (bar_width - filled)

        self.clear_screen()
        print(
            Color.BOLD + Color.PRIMARY + f"[ {bar} ] "
            + f"{percentage:6.2f} % " + Color.RESET
        )
        print()
        print(
            Color.PRIMARY + " ⟨ "
            + Color.GREEN + f"{self.attempts:,}" +  Color.PRIMARY + " / " + Color.RESET
            + Color.RED + f"{total_combinations:,}"
            + Color.PRIMARY + " ⟩ " + Color.DIM + "attempts" + Color.RESET
        )

    def print_success(self, password, length):
        print()

        colors = [
            Color.YELLOW, Color.BLUE, Color.GREEN,
            Color.PINK, Color.PURPLE, Color.RED,
        ]

        for revealed_count in range(length + 1):
            characters = []

            for i in range(length):
                if i < revealed_count:
                    characters.append(Color.PRIMARY + password[i] + Color.RESET)
                else:
                    characters.append(colors[i % len(colors)] + "*" + Color.RESET)

            output = " ".join(characters)

            print(
                "\r" +Color.PRIMARY + "Password Breached : ⟨ " + output + Color.PRIMARY + " ⟩" + Color.RESET,
                end="",
                flush=True,
            )
            time.sleep(0.2)

        print()

if __name__ == "__main__":
    vault = PasswordVault(password = PASSWORD)
    void = BruteBeetle(vault=vault)
    void.crack(length=len(PASSWORD))