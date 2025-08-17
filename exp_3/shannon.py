def shannon_fano(probabilities):
    # Normalize probabilities just in case
    total = sum(probabilities)
    if total == 0:
        raise ValueError("Sum of probabilities cannot be zero.")
    probabilities = [p / total for p in probabilities]

    def recursive_sf(p_list):
        if len(p_list) == 1:
            return ["0"]
        elif len(p_list) == 2:
            return ["0", "1"]

        # Sort in descending order and track original indices
        sorted_p = sorted(enumerate(p_list), key=lambda x: x[1], reverse=True)
        indices, p_sorted = zip(*sorted_p)

        # Find split point (closest to equal probability sum)
        cumulative_sum = 0
        total_sum = sum(p_sorted)
        split_index = 0
        for i, p in enumerate(p_sorted):
            cumulative_sum += p
            if cumulative_sum >= total_sum / 2:
                split_index = i + 1
                break

        # Ensure valid split (not empty left or right)
        if split_index <= 0:
            split_index = 1
        if split_index >= len(p_sorted):
            split_index = len(p_sorted) - 1

        left = p_sorted[:split_index]
        right = p_sorted[split_index:]

        left_codes = recursive_sf(left)
        right_codes = recursive_sf(right)

        new_codes = ["0" + code for code in left_codes] + ["1" + code for code in right_codes]

        # Reconstruct full code list in original order
        full_codes = [""] * len(p_list)
        for idx, code in zip(indices, new_codes):
            full_codes[idx] = code
        return full_codes

    # Generate the codewords
    codewords = recursive_sf(probabilities)

    # Compute the average codeword length
    average_length = sum(len(codewords[i]) * probabilities[i] for i in range(len(probabilities)))
    return codewords, average_length
symbols = ['A', 'B', 'C', 'D', 'E']
probabilities = [0.4, 0.2, 0.2, 0.1, 0.1]

codes, avg_len = shannon_fano(probabilities)

print("Symbol\tProbability\tCode")
for s, p, c in zip(symbols, probabilities, codes):
    print(f"{s}\t{p:.2f}\t\t{c}")
print(f"\nAverage Codeword Length: {avg_len:.4f} bits/symbol")
