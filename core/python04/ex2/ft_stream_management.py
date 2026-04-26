import sys


def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    # end means dont jump a line and put input next to the text no mine
    # flush=True is to prioritize showing the print TEXT before anything else
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)

    arch = input()

    status = input("Input Stream active. Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {arch}: {status}")

    # sys.stderr prints the message (in red) in the output indicating an error
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr,
    )
    print("[STANDARD] Data tranmission complete")
    print()

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_vault_security()
