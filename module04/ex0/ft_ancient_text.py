

if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print("\nAccessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        file = open("ancient_fragment.txt", "r")
        read = file.read()
        print(read)
    except Exception as err:
        print(f"Error: {err}")
        file = None
    finally:
        print("\nData recovery complete. Storage unit disconnected.")
        if file:
            file.close()
