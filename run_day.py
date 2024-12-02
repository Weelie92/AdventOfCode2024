import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path

    def on_modified(self, event):
        if event.src_path == self.script_path:
            print(f"\n[INFO] Detected changes in {self.script_path}. Re-running script...")
            subprocess.run(["python", self.script_path], check=True)

def run_and_watch(day: int, part: int):
    """
    Run and watch the specified part of a day.

    Args:
        day (int): The day number (e.g., 1 for "Day 1").
        part (int): The part to run (e.g., 1 for "Part1").
    """
    day_folder = f"Day {day}"
    script_name = f"Part{part}.py"
    script_path = os.path.abspath(os.path.join(day_folder, script_name))

    if not os.path.exists(script_path):
        print(f"[ERROR] The script {script_path} does not exist.")
        return

    print(f"[INFO] Running {script_name} in {day_folder}...")
    subprocess.run(["python", script_path], check=True)

    # Set up the watcher
    event_handler = FileChangeHandler(script_path)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(script_path), recursive=False)
    print(f"[INFO] Watching for changes in {script_path}... Press Ctrl+C to stop.")
    try:
        observer.start()
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("\n[INFO] Stopped watching for changes.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run and watch Part1 or Part2 for a specific Day.")
    parser.add_argument("day", type=int, help="The day number to run (e.g., 1 for 'Day 1').")
    parser.add_argument("part", type=int, choices=[1, 2], help="The part to run (e.g., '1' or '2').")
    args = parser.parse_args()

    try:
        run_and_watch(args.day, args.part)
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Script execution failed with exit code {e.returncode}.")
