# Show only the first few and last few digits
def summarize_large_number(n):
    s = str(n)
    if len(s) > 20:
        return f"{s[:10]}...{s[-10:]} (length: {len(s)})"
    return s

print(summarize_large_number(123456789012345678901234567890))