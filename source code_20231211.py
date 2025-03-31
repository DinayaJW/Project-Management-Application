def menu():
    """Display the main menu for XYZ Company Project Management System."""
    menu_text = """
                                     XYZ Company
                                      Main Menu

    1. Add a new project to existing projects
    2. Remove a completed project from existing projects
    3. Add new workers to available workers group
    4. Update details on ongoing projects
    5. Project Statistics
    6. Exit
    """
    print(menu_text)


def add_project(ongoing, onhold, completed):
    """Add a new project to the system."""
    pcode = int(input("Enter project Code (0 to cancel): "))
    if pcode <= 0:
        return False
    
    project = {
        "project_code": pcode,
        "client_name": input("Enter Client's name: "),
        "starting_date": input("Enter the relevant starting date: "),
        "ending_date": input("Enter the relevant ending date: "),
        "no_of_workers": int(input("Number of Workers: ")),
        "status": input("Project Status (Ongoing, OnHold, Completed): ").lower()
    }
    
    # Add project to the appropriate list based on status
    if project["status"] == "ongoing":
        ongoing.append(project)
    elif project["status"] == "onhold":
        onhold.append(project)
    elif project["status"] == "completed":
        completed.append(project)
    else:
        print("Invalid status. Project categorized as Ongoing by default.")
        project["status"] = "ongoing"
        ongoing.append(project)
    
    print("Project details:")
    for key, value in project.items():
        print(f"{key}: {value}")
    
    if input("Do you want to save the file (Yes or No)? ").lower() == "yes":
        print("Record Saved successfully")
        return True
    return False


def remove_project(completed):
    """Remove a completed project from the system."""
    if not completed:
        print("No completed projects to remove.")
        return
    
    print("Completed Projects:")
    for i, project in enumerate(completed):
        print(f"{i+1}. Project Code: {project['project_code']}, Client: {project['client_name']}")
    
    pcode = int(input("Enter project Code to remove: "))
    
    # Find the project to remove
    project_to_remove = None
    for project in completed:
        if project["project_code"] == pcode:
            project_to_remove = project
            break
    
    if project_to_remove:
        if input("Do you want to remove the project (Yes or No)? ").lower() == "yes":
            completed.remove(project_to_remove)
            print(f"Project {pcode} removed successfully")
    else:
        print(f"Project with code {pcode} not found in completed projects.")


def add_workers(available_workers):
    """Add new workers to the available workers pool."""
    try:
        workers_to_add = int(input("Enter the number of workers to add: "))
        if workers_to_add <= 0:
            print("Please enter a positive number.")
            return available_workers
        
        if input("Do you want to add new workers (Yes or No)? ").lower() == "yes":
            available_workers += workers_to_add
            print(f"{workers_to_add} new workers added successfully. Total available: {available_workers}")
        
        return available_workers
    except ValueError:
        print("Please enter a valid number.")
        return available_workers


def update_project(ongoing, onhold, completed):
    """Update details of an existing project."""
    # Display all projects
    all_projects = ongoing + onhold + completed
    if not all_projects:
        print("No projects to update.")
        return
    
    print("Current Projects:")
    for i, project in enumerate(all_projects):
        print(f"{i+1}. Project Code: {project['project_code']}, Client: {project['client_name']}, Status: {project['status']}")
    
    pcode = int(input("Enter project Code to update (0 to cancel): "))
    if pcode <= 0:
        return
    
    # Find the project to update
    project_to_update = None
    project_list = None
    for project_list_candidate in [ongoing, onhold, completed]:
        for project in project_list_candidate:
            if project["project_code"] == pcode:
                project_to_update = project
                project_list = project_list_candidate
                break
        if project_to_update:
            break
    
    if not project_to_update:
        print(f"Project with code {pcode} not found.")
        return
    
    # Remove from current list
    project_list.remove(project_to_update)
    
    # Get updated information
    updated_project = {
        "project_code": pcode,
        "client_name": input(f"Enter Client's name [{project_to_update['client_name']}]: ") or project_to_update['client_name'],
        "starting_date": input(f"Enter the relevant starting date [{project_to_update['starting_date']}]: ") or project_to_update['starting_date'],
        "ending_date": input(f"Enter the relevant ending date [{project_to_update['ending_date']}]: ") or project_to_update['ending_date'],
        "no_of_workers": int(input(f"Number of Workers [{project_to_update['no_of_workers']}]: ") or project_to_update['no_of_workers']),
        "status": input(f"Project Status (Ongoing, OnHold, Completed) [{project_to_update['status']}]: ").lower() or project_to_update['status']
    }
    
    # Add to appropriate list based on updated status
    if updated_project["status"] == "ongoing":
        ongoing.append(updated_project)
    elif updated_project["status"] == "onhold":
        onhold.append(updated_project)
    elif updated_project["status"] == "completed":
        completed.append(updated_project)
    else:
        print(f"Invalid status. Project kept as {project_to_update['status']}.")
        updated_project["status"] = project_to_update["status"]
        if updated_project["status"] == "ongoing":
            ongoing.append(updated_project)
        elif updated_project["status"] == "onhold":
            onhold.append(updated_project)
        else:
            completed.append(updated_project)
    
    print("Updated project details:")
    for key, value in updated_project.items():
        print(f"{key}: {value}")
    
    if input("Confirm updates (Yes or No)? ").lower() == "yes":
        print("Record Updated successfully")


def show_statistics(ongoing, onhold, completed, available_workers):
    """Display project statistics."""
    print("\n----- Project Statistics -----")
    print(f"Number of ongoing projects: {len(ongoing)}")
    print(f"Number of completed projects: {len(completed)}")
    print(f"Number of onhold projects: {len(onhold)}")
    print(f"Number of available workers to assign: {available_workers}")
    print("-----------------------------\n")


def main():
    """Main function to run the project management system."""
    # Initialize variables
    ongoing = []
    onhold = []
    completed = []
    available_workers = 0
    
    while True:
        menu()
        try:
            option = int(input("Please enter your option (1-6): "))
            
            if option == 1:
                add_project(ongoing, onhold, completed)
            elif option == 2:
                remove_project(completed)
            elif option == 3:
                available_workers = add_workers(available_workers)
            elif option == 4:
                update_project(ongoing, onhold, completed)
            elif option == 5:
                show_statistics(ongoing, onhold, completed, available_workers)
            elif option == 6:
                print("Exiting the system...")
                print("Thank you, Have a nice day!!")
                break
            else:
                print("Please enter a valid number between 1-6")
        except ValueError:
            print("Please enter a valid number between 1-6")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
