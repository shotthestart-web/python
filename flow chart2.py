def daily_routine_flowchart():
    # Start
    print("[START] Wake up and turn off alarm")
    
    # Process 1
    print(" -> Brush teeth and wash face")
    
    # Decision
    is_school_or_work = input("Is it a weekday (yes/no)? ").strip().lower()
    
    if is_school_or_work == "yes":
        # Yes Branch
        print(" -> [YES] Eat quick breakfast")
        print(" -> Get dressed and pack bag")
        print(" -> Go to school or work")
    else:
        # No Branch
        print(" -> [NO] Relax and make a big breakfast")
        print(" -> Do hobbies or exercise")
        
    # Merge & Final Processes
    print(" -> Eat dinner")
    print(" -> Brush teeth and get ready for bed")
    
    # End
    print("[END] Go to sleep")

# Run the flowchart
daily_routine_flowchart()