def ft_vault_security() -> None:
    """
    The 'with' statement automatically closes files even
    if errors occur, preventing data corruption and resource leaks
    """
    try:
        with open(
            "classified_data.txt"
        ) as txt_file:  # automatically closes the file
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")
            print()

            print("SECURE EXTRACTION:")
            print(txt_file.read())
            print()

            try:
                with open("security_protocols.txt") as second_txt_file:
                    print("SECURE PRESERVATION:")
                    print(second_txt_file.read())
                    print("Vault automatically sealed upon completion")
                    print()
            except FileNotFoundError:
                print("Error: file security_protocols.txt not found")
                return

            print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("Error: file classified_data.txt not found")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()

    ft_vault_security()
