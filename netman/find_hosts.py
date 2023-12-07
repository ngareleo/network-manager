import subprocess
import re


def crunch_ping_response(data: str) -> dict[str, str]:
    # TODO: Execute all these searches simultenously
    return {
        "host": re.search(r"Ping\sstatistics\sfor\s(?P<host>.+):", data)["host"],
        "sent": re.search(r"Sent\s=\s(?P<sent>\d+)", data)["sent"],
        "recv": re.search(r"Received\s=\s(?P<recv>\d+)", data)["recv"],
        "lost": re.search(r"Lost\s=\s(?P<lost>\d+)", data)["lost"],
        "loss": re.search(r"\((?P<loss>\d+)%\sloss\)", data)["loss"],
    }


def ping_host(host: str) -> dict[str, str]:
    out = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        timeout=5,
        universal_newlines="\n",
    ).stdout

    return crunch_ping_response(out)


if __name__ == "__main__":
    for i in range(1, 11):
        ping = ping_host(f"192.168.100.{i}")
        res = crunch_ping_response(ping)

