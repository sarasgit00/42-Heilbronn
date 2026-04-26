def ft_ancient_text() -> None:
    try:
        txt_file = open("ancient_fragment.txt", "r")  # mode 'r' is read
        # we domt want to accidentally write so we open in mode "read"
        print(f"Accessing Storage Vault: {txt_file.name}")
        print("Connection established...")
        content_file = txt_file.read()
        # with the method "read" we read the content of the file
        print()

        print("RECOVERED DATA:")
        print(content_file)
        txt_file.close()
        # we close because of memory leaks, its like free

        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"Could not open {txt_file.name} file")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()

    ft_ancient_text()
