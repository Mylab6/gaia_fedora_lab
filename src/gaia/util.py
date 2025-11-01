# Copyright(C) 2024-2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT

import platform
import subprocess
import time


def kill_process_on_port(port):
    """Kill any process running on the specified port.
    
    Cross-platform implementation supporting Windows, Linux (Ubuntu, Debian, Fedora, etc.), and other Unix-like systems.
    """
    try:
        system = platform.system()
        pids_to_kill = set()
        
        if system == "Windows":
            # Windows: Use netstat and taskkill
            result = subprocess.run(
                f"netstat -ano | findstr :{port}",
                shell=True,
                capture_output=True,
                text=True,
                check=False,
            )

            if result.stdout:
                # Extract PID
                for line in result.stdout.strip().split("\n"):
                    if f":{port}" in line and (
                        "LISTENING" in line or "ESTABLISHED" in line
                    ):
                        parts = line.strip().split()
                        if len(parts) > 4:
                            pid = parts[-1]
                            pids_to_kill.add(pid)

                # Kill each process found
                for pid in pids_to_kill:
                    print(f"Found process with PID {pid} on port {port}")
                    try:
                        subprocess.run(f"taskkill /F /PID {pid}", shell=True, check=False)
                        print(f"Killed process with PID {pid}")
                    except Exception as e:
                        print(f"Error killing PID {pid}: {e}")
        else:
            # Linux/Unix (including Ubuntu, Debian, Fedora, CentOS, etc.)
            # Try lsof first (more reliable if available)
            result = subprocess.run(
                f"lsof -ti :{port}",
                shell=True,
                capture_output=True,
                text=True,
                check=False,
            )
            
            if result.stdout:
                pids_to_kill = set(result.stdout.strip().split("\n"))
            else:
                # Fallback to netstat if lsof is not available
                result = subprocess.run(
                    f"netstat -tlnp 2>/dev/null | grep ':{port} ' || netstat -tulnp 2>/dev/null | grep ':{port} '",
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                
                if result.stdout:
                    for line in result.stdout.strip().split("\n"):
                        # Extract PID from netstat output
                        parts = line.strip().split()
                        if len(parts) > 6:
                            # PID/Program name is typically the last column
                            pid_prog = parts[-1]
                            if "/" in pid_prog:
                                pid = pid_prog.split("/")[0]
                                if pid.isdigit():
                                    pids_to_kill.add(pid)
            
            # Kill each process found
            for pid in pids_to_kill:
                if pid and pid.isdigit():
                    print(f"Found process with PID {pid} on port {port}")
                    try:
                        subprocess.run(f"kill -9 {pid}", shell=True, check=False)
                        print(f"Killed process with PID {pid}")
                    except Exception as e:
                        print(f"Error killing PID {pid}: {e}")

        # Give the OS some time to free the port
        if pids_to_kill:
            time.sleep(2)
        else:
            print(f"No process found listening on port {port}")
    except Exception as e:
        print(f"Error killing process on port {port}: {e}")
