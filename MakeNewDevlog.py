import time
from pathlib import Path
import os
from colorama import init, Fore

# Initialize colorama for colored console output
init(autoreset=True)

# Get current time for formatting and file naming
current_time = time.localtime()
current_script_dir = Path(__file__).parent  # Directory of the current script

# Formatted date and time strings for titles and filenames
formatted_datetime = time.strftime("%d-%m-%Y_%H-%M", current_time)
formatted_date = time.strftime("%d-%m-%Y", current_time)
formatted_time = time.strftime("%H-%M", current_time)

# Define the path for the logs directory
logs_dir = current_script_dir / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)  # Ensure logs directory exists

# Function to determine the next available log index based on existing files
def get_next_log_index(logs_path):
    log_files = list(logs_path.glob("*.md"))
    indices = []

    for log_file in log_files:
        try:
            # Extract index from filenames of the format 'index__date_time.md'
            index_part = log_file.stem.split("__")[0]
            if index_part.isdigit():
                indices.append(int(index_part))
        except ValueError:
            continue

    # Return the next index, starting from 1 if no files exist
    return max(indices, default=0) + 1

# Calculate the next log file index
next_log_index = get_next_log_index(logs_dir)

# Path to the template file
template_path = current_script_dir / "template.md"

# Read the template content
try:
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
except FileNotFoundError:
    print(Fore.RED + f"Template file 'template.md' not found in {current_script_dir}.")
    exit()

# Display current log information to the user
print(f"Current log index: {next_log_index} || Date: {formatted_date} || Time: {formatted_time}\n")

# Prompt the user for the log title
log_title = input("Enter the title of the devlog: ")

# Replace placeholders in the template with actual values
template_content = template_content.replace("Nr.", str(next_log_index))
template_content = template_content.replace("Title", log_title)
template_content = template_content.replace("YYYY-MM-DD", formatted_date)
template_content = template_content.replace("HH:MM", formatted_time)

# Generate the new log file name
log_filename = f"{next_log_index}__{formatted_datetime}.md"
new_log_path = logs_dir / log_filename

# Ask the user whether to enter log content manually
def get_multiline_input(prompt):
    """Prompt the user for multi-line input and return as a formatted string."""
    print(f"Enter content for '{prompt}'. Type 'done' or 'end' to finish:")
    lines = []
    while True:
        line = input("- ")
        if line.lower() in {"done", "end"}:
            break
        lines.append(line)
    return '\n- '.join(lines)

manual_entry_choice = input("Do you want to enter the log content manually? (y/n): ").strip().lower()
if manual_entry_choice == "y":
    # Collect content for each section
    lessons_learned = get_multiline_input("Lessons learned")
    what_i_did = get_multiline_input("What I did")
    challenges_faced = get_multiline_input("Challenges faced")
    next_steps = get_multiline_input("Next steps")

    # Replace section placeholders in the template
    template_content = template_content.replace("### Lessons learned:\n- ", f"### Lessons learned:\n- {lessons_learned}")
    template_content = template_content.replace("### What I did:\n- ", f"### What I did:\n- {what_i_did}")
    template_content = template_content.replace("### Challenges faced:\n- ", f"### Challenges faced:\n- {challenges_faced}")
    template_content = template_content.replace("### Next steps:\n- ", f"### Next steps:\n- {next_steps}")
else:
    print("Skipping manual content entry.")

# Write the updated content to the new log file
with open(new_log_path, "w") as log_file:
    log_file.write(template_content)

print(Fore.GREEN + f"New log file created: {log_filename} in '{logs_dir}'")