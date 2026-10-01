import re
import unicodedata
import pandas as pd


def normalize_text(value):
    """Normalize text for entity matching."""
    if pd.isna(value):
        return ""

    text = str(value).casefold().strip()

    # Normalize Unicode and remove accent marks
    text = unicodedata.normalize("NFKD", text)
    text = "".join(
        char for char in text
        if not unicodedata.combining(char)
    )

    # Replace punctuation with spaces
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def preprocess_businesses(df):
    """Add normalized matching features to business records."""
    required = {
        "entity_id",
        "business_name",
        "business_address",
        "country"
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    result = df.copy()

    result["name_norm"] = (
        result["business_name"].map(normalize_text)
    )
    result["address_norm"] = (
        result["business_address"].map(normalize_text)
    )
    result["country_norm"] = (
        result["country"].fillna("").astype(str).str.strip().str.upper()
    )

    return result
