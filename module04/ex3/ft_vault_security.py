

if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
        print("\nInitiating secure vault access...")
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt", "r") as file1:
            read1 = file1.read()
            print(read1)
    except Exception as err:
        print(f"Error: {err}")
    try:
        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as file2:
            content = "[CLASSIFIED] New security protocols archived"
            file2.write(f"{content}")
            print(content)
        print("Vault automatically sealed upon completion")
    except Exception as err:
        print(f"Error: {err}")
    finally:
        print("\nAll vault operations completed with maximum security.")
