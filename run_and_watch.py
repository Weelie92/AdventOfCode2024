import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == os.path.abspath(self.script_path):
            print(f"\n[INFO] Detected changes in {self.script_path}. Re-running script...")
            try:
                subprocess.run(["python", self.script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Script execution failed with exit code {e.returncode}.")


def run_and_watch(day: int, part: int, observer: Observer = None):
    """
    Run and watch the specified part of a day.

    Args:
        day (int): The day number (e.g., 1 for "Day 1").
        part (int): The part to run (e.g., 1 for "Part1").
        observer (Observer): Existing observer instance (if restarting).
    """
    day_folder = f"Day {day}"
    script_name = f"Part{part}.py"
    script_path = os.path.abspath(os.path.join(day_folder, script_name))

    if not os.path.exists(script_path):
        print(f"[ERROR] The script {script_path} does not exist.")
        return False

    print(f"[INFO] Running {script_name} in {day_folder}...")
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Script execution failed with exit code {e.returncode}.")

    # Stop the previous observer if it exists
    if observer:
        observer.stop()
        observer.join()

    # Set up a new watcher
    event_handler = FileChangeHandler(script_path)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(script_path), recursive=False)
    print(f"[INFO] Watching for changes in {script_path}... Type 'day part' to switch or 'exit' to quit.")
    observer.start()

    return observer


def interactive_mode(initial_day: int, initial_part: int):
    """
    Interactive mode to switch between days and parts after starting.

    Args:
        initial_day (int): The initial day number to start watching.
        initial_part (int): The initial part number to start watching.
    """
    observer = None
    current_day, current_part = initial_day, initial_part

    try:
        # Start with the initial day and part
        observer = run_and_watch(current_day, current_part)

        while True:
            user_input = input("\nEnter 'day part' to switch or 'exit' to quit: ").strip()
            if user_input.lower() == "exit":
                print("[INFO] Exiting interactive mode.")
                break

            try:
                # Parse day and part from input
                day, part = map(int, user_input.split())
                if part not in [1, 2]:
                    print("[ERROR] Part must be 1 or 2. Try again.")
                    continue

                # Restart watcher with new day and part
                observer = run_and_watch(day, part, observer)
                current_day, current_part = day, part
            except ValueError:
                print("[ERROR] Invalid input. Please enter in the format 'day part' (e.g., '1 2').")
    except KeyboardInterrupt:
        print("\n[INFO] Exiting interactive mode.")
    finally:
        # Ensure observer stops
        if observer:
            observer.stop()
            observer.join()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run and watch Part1 or Part2 for a specific Day.")
    parser.add_argument("day", type=int, help="The day number to run (e.g., 1 for 'Day 1').")
    parser.add_argument("part", type=int, choices=[1, 2], help="The part to run (e.g., '1' or '2').")
    args = parser.parse_args()

    interactive_mode(args.day, args.part)
