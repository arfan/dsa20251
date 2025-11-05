import time
import itertools

def brute_force_password(target: str,
                         charset: str = "abcdefghijklmnopqrstuvwxyz0123456789",
                         length: int = 4,
                         show_progress: bool = False):
    """
    Attempt every combination from 'charset' of given 'length' to find 'target'.
    This is a local, in-memory demo: the function compares strings only.
    """
    if len(target) != length:
        raise ValueError(f"Target length ({len(target)}) != requested brute-force length ({length}).")

    start = time.time()
    attempts = 0
    total = len(charset) ** length

    # Use itertools.product to generate combinations in lexicographic order
    for combo in itertools.product(charset, repeat=length):
        attempts += 1
        guess = ''.join(combo)
        print("guess:", guess)
        if show_progress and attempts % 10000 == 0:
            elapsed = time.time() - start
            print(f"[{attempts}/{total}] tries, elapsed {elapsed:.2f}s, last guess: {guess}")
        if guess == target:
            elapsed = time.time() - start
            return {
                "found": True,
                "password": guess,
                "attempts": attempts,
                "elapsed_seconds": elapsed
            }

    elapsed = time.time() - start
    return {"found": False, "attempts": attempts, "elapsed_seconds": elapsed}

if __name__ == "__main__":
    demo_target = "a1b2"               # must be exactly length 4 here
    demo_charset = "abcd0123"          # small charset for quick demo
    result = brute_force_password(demo_target, charset=demo_charset, length=4, show_progress=True)

    if result["found"]:
        print(f"Password found: {result['password']} in {result['attempts']} attempts, {result['elapsed_seconds']:.4f}s")
    else:
        print(f"Password NOT found after {result['attempts']} attempts, {result['elapsed_seconds']:.4f}s")