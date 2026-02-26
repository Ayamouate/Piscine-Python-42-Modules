

if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print("\nInitializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        file = open("new_discovery.txt", "w")
        content = ("[ENTRY 001] New quantum algorithm discovered\n"
                   "[ENTRY 002] Efficiency increased by 347%\n"
                   "[ENTRY 003] Archived by Data Archivist trainee\n")
        file.write(content)
        print(content)
    except Exception as err:
        print(f"Error: {err}")
        file = None
    finally:
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
        if file:
            file.close()
