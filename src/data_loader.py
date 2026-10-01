from pathlib import Path
import pandas as pd


def read_tsv_chunks(path, chunksize=100_000):
    """Read a large TSV file in manageable chunks."""
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(
        path,
        sep="\t",
        chunksize=chunksize,
        dtype="string",
        keep_default_na=True,
    )


def inspect_tsv(path):
    """Inspect a TSV file without loading the entire dataset."""
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    sample = pd.read_csv(path, sep="\t", nrows=5)

    return {
        "file": path.name,
        "size_mb": round(path.stat().st_size / 1024**2, 2),
        "columns": sample.columns.tolist(),
        "sample": sample,
    }
