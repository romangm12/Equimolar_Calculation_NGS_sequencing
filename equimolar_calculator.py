"""Equimolar pooling calculator for DNA fragments or amplicons.

This command-line tool estimates how many microliters of each DNA fragment
should be mixed so every fragment contributes the same number of molecules.
"""

from dataclasses import dataclass


MAX_VALUE = 1_000_000
DSDNA_MW_PER_BP = 617.96
DSDNA_MW_ENDS = 36.04


@dataclass
class Fragment:
    name: str
    length_bp: int
    mass_ng: float
    volume_ul: float

    @property
    def molecular_weight(self) -> float:
        """Approximate molecular weight for double-stranded DNA."""
        return (self.length_bp * DSDNA_MW_PER_BP) + DSDNA_MW_ENDS

    @property
    def concentration_ng_ul(self) -> float:
        return self.mass_ng / self.volume_ul

    @property
    def concentration_fmol_ul(self) -> float:
        # ng/uL -> g/uL -> mol/uL -> fmol/uL
        return (self.concentration_ng_ul * 1e-9 / self.molecular_weight) * 1e15

    @property
    def total_fmol(self) -> float:
        return self.concentration_fmol_ul * self.volume_ul


def read_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")
            continue

        if 0 < value <= MAX_VALUE:
            return value

        print(f"Please enter a value greater than 0 and lower than {MAX_VALUE}.")


def read_positive_int(prompt: str) -> int:
    while True:
        value = read_positive_float(prompt)
        if value.is_integer():
            return int(value)
        print("Please enter a whole number.")


def collect_fragments() -> list[Fragment]:
    fragment_count = read_positive_int("How many fragments or amplicons? ")
    fragments = []

    for index in range(1, fragment_count + 1):
        print(f"\nFragment {index}")
        name = input("Name: ").strip() or f"DNA{index}"
        length_bp = read_positive_int("Length (bp): ")
        mass_ng = read_positive_float("Total mass available (ng): ")
        volume_ul = read_positive_float("Total volume available (uL): ")
        fragments.append(Fragment(name, length_bp, mass_ng, volume_ul))

    return fragments


def calculate_pooling_volumes(fragments: list[Fragment]) -> list[tuple[Fragment, float]]:
    target_fmol = min(fragment.total_fmol for fragment in fragments)
    return [
        (fragment, target_fmol / fragment.concentration_fmol_ul)
        for fragment in fragments
    ]


def print_results(fragments: list[Fragment]) -> None:
    pooling_volumes = calculate_pooling_volumes(fragments)
    total_pool_volume = sum(volume for _, volume in pooling_volumes)

    print("\nEquimolar pooling results")
    print("-" * 60)
    print(f"{'Fragment':<16}{'fmol/uL':>12}{'Use uL':>12}{'Available uL':>16}")
    print("-" * 60)

    for fragment, volume_ul in pooling_volumes:
        print(
            f"{fragment.name:<16}"
            f"{fragment.concentration_fmol_ul:>12.3f}"
            f"{volume_ul:>12.2f}"
            f"{fragment.volume_ul:>16.2f}"
        )

    print("-" * 60)
    print(f"Final pool volume: {total_pool_volume:.2f} uL")
    print("Each fragment contributes the same femtomoles to the final pool.")


def main() -> None:
    print("NGS equimolar pooling calculator")
    fragments = collect_fragments()
    print_results(fragments)


if __name__ == "__main__":
    main()
