"""Rough cognify benchmark: run against a fixture dataset and print phase timings."""
import time


def bench(n_docs: int = 100) -> None:
    start = time.perf_counter()
    # placeholder: wire to cognee.cognify() over a fixture corpus
    elapsed = time.perf_counter() - start
    print(f"cognify over {n_docs} docs: {elapsed:.2f}s")


if __name__ == "__main__":
    bench()
