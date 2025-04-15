import subprocess, signal

def run(code: str):
    with open("user_code.py", "w") as f:
        f.write(code)

    def timeout(s, f): raise TimeoutError("timeout")
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(3)

    try:
        p = subprocess.run(["python3", "user_code.py"], capture_output=True, text=True)
        signal.alarm(0)
        return p.stdout, p.stderr
    except TimeoutError:
        return "", "timeout"
    except Exception as e:
        return "", str(e)
