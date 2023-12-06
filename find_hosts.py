import subprocess
import re


class HostTemplate:
    pass


def prettify_response_ping_res(host_template: str, n: tuple[int, int]) -> None:
    """Returns a table row of the reponse simplified"""

    print(f'##{"#"*15}###{"#"*5}###{"#"*6}###{"#"*7}###{"#"*6}##')  # top
    print(f'# {"Host":15} # {"Sent":5} # {"Recieved":6} # {"Lost":7} # {"Loss":6} #')
    print(f'##{"#"*15}###{"#"*5}###{"#"*6}###{"#"*7}###{"#"*6}##')  # top
    lead, trail = n
    print("#", end="")
    for i in range(lead, trail + 1):
        infos = ping_host(f"{host_template}.{i}")
        for _, value in infos.items():
            print(f" {value} ", end="")
            print("#", end="")
        status = "Online" if (int(infos["loss"]) == 0) else "Offline"
        print("#")
    print(f'##{"#"*15}###{"#"*5}###{"#"*6}###{"#"*7}###{"#"*6}##')  # top


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
    prettify_response_ping_res("192.168.100", (1, 10))
