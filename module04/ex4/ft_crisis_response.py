
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", 'r') as file1:
            print("File found")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except Exception:
        print("Other errors accured: 404")
    finally:
        print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", 'r') as file2:
            print("Permission successed")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("Other errors accured: 405")
    finally:
        print("STATUS: Crisis handled, security maintained")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", 'r') as file3:
            reading = file3.read()
            print(f"SUCCESS: Archive recovered - ``{reading}''")
            print("STATUS: Normal operations resumed")
    except Exception:
        print("Other errors accured: 406")
    finally:
        print("\nAll crisis scenarios handled successfully. Archives secure.")
