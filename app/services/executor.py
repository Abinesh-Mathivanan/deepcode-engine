import subprocess
import uuid
import os
import time

def run_code(code: str, fn: str, test_cases: list):
    file = f"/tmp/{uuid.uuid4().hex}.py"
    with open(file, "w") as f:
        f.write(code + "\n")

        for i, t in enumerate(test_cases):
            f.write(f'print("{i}>>>" + str({fn}({t["input"]})))\n')

    try:
        start = time.time()
        res = subprocess.run(
            ["python3", file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3,
            check=False,
        )
        end = time.time()
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if os.path.exists(file):
            os.remove(file)

    output = res.stdout.decode()
    error = res.stderr.decode()

    results = []
    for line in output.splitlines():
        if ">>>" in line:
            idx, out = line.split(">>>", 1)
            try:
                passed = out.strip() == str(test_cases[int(idx)]["expected_output"]).strip()
            except:
                passed = False
            results.append({
                "input": test_cases[int(idx)]["input"],
                "expected": test_cases[int(idx)]["expected_output"],
                "actual": out.strip(),
                "passed": passed
            })

    return {"results": results, "error": error if error else None, "time": round(end - start, 3)}
