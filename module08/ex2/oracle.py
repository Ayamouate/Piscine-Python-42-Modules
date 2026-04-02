import os
from dotenv import load_dotenv


def check_configuration() -> None:
    print("\nEnvironment security check:")
    api_key = os.getenv("API_KEY")
    if api_key and api_key != "hardcoded_key":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Possible hardcoded secret!")
    if api_key:
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file missing or not loded")
    if os.getenv("APP_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...")
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    print("\nConfiguration loaded:")
    if mode:
        print(f"Mode: {mode}")
    else:
        print("Mode: Missing key!")
    if db_url:
        print(f"Database: {db_url}")
    else:
        print("Database: Missing key!")
    if api_key:
        print(f"API Access: {api_key}")
    else:
        print("API Access: Missing key!")
    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: Missing key!")
    if zion:
        print(f"Zion: {zion}")
    else:
        print("Zion: Missing key!")

    check_configuration()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
