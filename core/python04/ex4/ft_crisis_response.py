"""Archive incident handler."""


def ft_crisis_response() -> None:
    """Process archive access events."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    archive_list: str = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt",
    ]

    for name in archive_list:
        print(f"\nChecking access for '{name}'...")

        if name == "lost_archive.txt":
            try:
                with open(name, "r"):
                    pass
            except FileNotFoundError:
                print("ALERT: Archive missing from system")
                print("RESULT: Issue contained, system secure")

        elif name == "classified_vault.txt":
            try:
                # Simulated restricted access
                # raise means execute the class permissionerrror
                raise PermissionError("Restricted file")
            except PermissionError:
                print("ALERT: Access blocked by security policy")
                print("RESULT: Security integrity preserved")

        elif name == "standard_archive.txt":
            try:
                with open(name, "r"):
                    print("INFO: Archive opened successfully")
                    print("RESULT: Operations normal")
            except Exception as err:
                print(f"ERROR: Unexpected failure -> {err}")


if __name__ == "__main__":
    ft_crisis_response()
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
