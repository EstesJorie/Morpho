def getModeSelection():
    """
    Returns:
        bool: True if TEST_MODE, False if USER_MODE
    """ 
    while True:
          print(f"Select mode:\n")
          print("1. TEST MODE (Preset values)\n")
          print("2. USER MODE (User values)\n")
          print("Enter '1' for TEST MODE or '2' for USER MODE.\n")
          choice = input("Enter choice: ").strip().lower()
          if choice in ['1', '2']:
               return choice == '1' # if choice = 1, then TRUE thus TEST_MODE = True
          raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")