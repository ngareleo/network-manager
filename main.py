from netman import *

if __name__ == "__main__":
    table = [["Host", "Sent", "Received", "Lost", "Loss"]]
    for i in range(1, 11):
        ping = ping_host(f"192.168.100.{i}")
        table.append(list(ping.values()))

    Table.draw_from_list(table)
