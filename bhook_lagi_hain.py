import subprocess

def run_bash_script(file_name):
  """Runs a bash script to install all requirements from requirements.txt"""
  subprocess.run(["sh", file_name])

def run_streamlit_file(file_name):
  """Runs a Python file as a separate process."""
  subprocess.run(["streamlit", "run", file_name])

def main():
    run_bash_script("run_app.sh")
    run_streamlit_file("bhojanGPT.py")

if __name__ == "__main__":
    main()
