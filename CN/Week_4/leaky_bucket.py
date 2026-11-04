n = 5
capacity = 4
outflow = 3
packets = [2, 4, 4, 5, 3]
remaining = [0 for _ in range(n)]
accepted = [0 for _ in range(n)]
sent = [0 for _ in range(n)]

def print_table():
    print("clock\t packet_size\t accept\t sent\t remaining\t")
    for i, value in enumerate(packets):
        print(f"{i+1}\t {packets[i]}\t\t {accepted[i]}\t {sent[i]}\t {remaining[i]}\t ")

def solve():
    for i, packet in enumerate(packets):
        if packet+remaining[i-1] > capacity:
            accepted[i] = -1
            remaining[i] = 0
            sent[i] = remaining[i-1]

        elif packet > outflow:
            accepted[i] = packet
            sent[i] = outflow
            remaining[i] = packet-outflow

        else:
            accepted[i] = packet
            sent[i] = packet + max(remaining[i-1], 0)
            remaining[i] = 0

solve()
print_table()
