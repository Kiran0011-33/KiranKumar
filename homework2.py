from fractions import Fraction


def fmt(x: Fraction) -> str:
    """Print integers cleanly and non-integers as decimals."""
    if x.denominator == 1:
        return str(x.numerator)
    return f"{float(x):.10f}".rstrip("0").rstrip(".")


def run_biquad(inputs):
    """
    Run the 5-cycle biquad example using a direct state-machine style.

    Equations:
        s[n] = X[n] + (1/8)F[n] + (1/8)H[n]
        Y[n] = (1/8)s[n] + (1/8)F[n] + (1/8)H[n]

    State update:
        F[n] = previous s[n-1]
        H[n] = previous-previous s[n-2]
    """

    # Initial states
    prev_s1 = Fraction(0, 1)   # acts like F[n] = s[n-1]
    prev_s2 = Fraction(0, 1)   # acts like H[n] = s[n-2]

    rows = []

    for cycle in range(len(inputs)):
        x_n = Fraction(inputs[cycle], 1)

        # Current internal values
        f_n = prev_s1
        h_n = prev_s2

        # Compute current stage/output
        s_n = x_n + (f_n + h_n) / 8
        y_n = (s_n + f_n + h_n) / 8

        rows.append({
            "cycle": cycle + 1,
            "X[n]": x_n,
            "F[n]": f_n,
            "H[n]": h_n,
            "s[n]": s_n,
            "Y[n]": y_n,
        })

        # Shift state for next cycle
        prev_s2 = prev_s1
        prev_s1 = s_n

    return rows


def print_results(rows):
    header = f"{'Cycle':<5} {'X[n]':>8} {'F[n]=s[n-1]':>14} {'H[n]=s[n-2]':>14} {'s[n]':>14} {'Y[n]':>16}"
    print(header)
    print("-" * len(header))

    for row in rows:
        print(
            f"{row['cycle']:<5} "
            f"{fmt(row['X[n]']):>8} "
            f"{fmt(row['F[n]']):>14} "
            f"{fmt(row['H[n]']):>14} "
            f"{fmt(row['s[n]']):>14} "
            f"{fmt(row['Y[n]']):>16}"
        )

    outputs = ", ".join(fmt(row["Y[n]"]) for row in rows)
    print("\nFive output samples:")
    print(outputs)


if __name__ == "__main__":
    inputs = [100, 5, 500, 20, 250]
    rows = run_biquad(inputs)

    print("EE 5393 Homework 2 — Problem 2 verification")
    print("Equations:")
    print("  s[n] = X[n] + (1/8)F[n] + (1/8)H[n]")
    print("  Y[n] = (1/8)s[n] + (1/8)F[n] + (1/8)H[n]")
    print("  F[n] = s[n-1],   H[n] = s[n-2]")
    print("  Initial conditions: F[1] = 0, H[1] = 0\n")

    print_results(rows)