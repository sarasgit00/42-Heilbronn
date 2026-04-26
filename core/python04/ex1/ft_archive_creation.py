def ft_archive_creation() -> None:
    try:
        txt_file = open(
            "new_discovery.txt", "w"
        )  # w = open in mode "overwrite" | a = open in mode "append"
        preservate_data = {
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee"
        }

        print(f"Initializing new storage unit: {txt_file.name}")
        print("Storage unit created successfully...")
        print()

        print("Inscribing preservation data...")
        for i in preservate_data:
            txt_file.write(i)
            print(i)

        print()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{txt_file.name}' ready for long-term preservation.")
    except Exception as e:
        print(e)
    finally:
        txt_file.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()

    ft_archive_creation()
