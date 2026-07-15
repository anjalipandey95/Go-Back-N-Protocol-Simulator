
import time
import random


def print_header():
    print("=" * 70)
    print("             GO-BACK-N PROTOCOL SIMULATOR (VERSION 5)")
    print("=" * 70)


def get_input():

    while True:

        try:

            total_packets = int(input("Enter Total Packets : "))
            window_size = int(input("Enter Window Size   : "))

            if total_packets <= 0:
                print("\nTotal packets must be greater than 0.\n")
                continue

            if window_size <= 0:
                print("\nWindow size must be greater than 0.\n")
                continue

            if window_size > total_packets:
                print("\nWindow size cannot be greater than total packets.\n")
                continue

            choice = input("\nUse Random Packet Loss? (y/n): ").lower()

            if choice == "y":
                lost_packet = random.randint(0, total_packets - 1)
                print(f"\nRandom Packet Selected : {lost_packet}")

            else:
                lost_packet = int(
                    input("Enter Lost Packet (-1 for no loss): ")
                )

                if lost_packet >= total_packets:
                    print("\nInvalid Lost Packet Number.\n")
                    continue

            return total_packets, window_size, lost_packet

        except ValueError:
            print("\nPlease enter only integer values.\n")


def simulate(total_packets, window_size, lost_packet):

    base = 0

    total_sent = 0
    delivered = 0
    lost = 0
    retransmission = 0
    ack_received = 0

    start_time = time.time()

    while base < total_packets:

        end = min(base + window_size, total_packets)

        print("\n" + "=" * 70)
        print("Current Sender Window : ", end="")

        for i in range(base, end):
            print(f"[{i}] ", end="")

        print("\n")

        packet_lost = False

        for packet in range(base, end):

            print(f"Sender  --> Sending Packet {packet}")

            total_sent += 1

            time.sleep(0.5)

            if packet == lost_packet:

                print(f"Network --> Packet {packet} Lost!")

                lost += 1
                packet_lost = True

                print()

                # Remaining packets are discarded by receiver
                for p in range(packet + 1, end):

                    print(f"Sender  --> Sending Packet {p}")

                    total_sent += 1

                    time.sleep(0.5)

                    print(
                        f"Receiver --> Packet {p} Discarded "
                        f"(Expected Packet {packet})"
                    )

                break

            else:

                print(f"Receiver --> Packet {packet} Received")

                delivered += 1

                print(f"Receiver --> ACK {packet + 1} Sent")

                print(f"Sender  <-- ACK {packet + 1} Received\n")

                ack_received += 1

        if packet_lost:

            print("\nTimeout Occurred...")

            time.sleep(1)

            print(f"\nGo Back To Packet {packet}")

            print("\nRetransmitting...\n")

            retransmission += (end - packet)

            for p in range(packet, end):

                print(f"Sender  --> Sending Packet {p}")

                total_sent += 1

                time.sleep(0.5)

                print(f"Receiver --> Packet {p} Received")

                delivered += 1

                print(f"Receiver --> ACK {p + 1} Sent")

                print(f"Sender  <-- ACK {p + 1} Received\n")

                ack_received += 1

            # Packet loss only once
            lost_packet = -1

        base = end

        end_time = time.time()

    total_time = end_time - start_time

    efficiency = (delivered / total_sent) * 100 if total_sent else 0

    print("\n" + "=" * 70)
    print("TRANSMISSION REPORT")
    print("=" * 70)

    print(f"Total Packets           : {total_packets}")
    print(f"Window Size             : {window_size}")
    print(f"Total Packets Sent      : {total_sent}")
    print(f"Delivered Packets       : {delivered}")
    print(f"Lost Packets            : {lost}")
    print(f"Retransmissions         : {retransmission}")
    print(f"ACK Received            : {ack_received}")
    print(f"Protocol Efficiency     : {efficiency:.2f}%")
    print(f"Transmission Time       : {total_time:.2f} Seconds")

    print("=" * 70)
    print("Transmission Completed Successfully")
    print("=" * 70)

def main():

    print_header()

    total_packets, window_size, lost_packet = get_input()

    simulate(
        total_packets,
        window_size,
        lost_packet
    )

    print("\nThank You For Using Go-Back-N Protocol Simulator.")


if __name__ == "__main__":
    main()