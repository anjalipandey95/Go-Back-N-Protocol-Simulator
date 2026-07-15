# Go-Back-N Protocol Simulator

## Overview

This project is a Command Line Interface (CLI) based implementation of the Go-Back-N Automatic Repeat Request (ARQ) Protocol using Python. It simulates reliable data transmission over a network using the Sliding Window Protocol. The simulator demonstrates packet transmission, packet loss, acknowledgements (ACK), timeout, retransmission, and transmission statistics.



## Features

- CLI (Command Line Interface) based simulator
- Sliding Window Protocol implementation
- Manual Packet Loss Simulation
- Random Packet Loss Simulation
- ACK Generation
- Timeout Mechanism
- Go-Back-N Retransmission
- Transmission Statistics
- Protocol Efficiency Calculation
- Input Validation



## Technologies Used

- Python 3
- Command Line Interface (CLI)



## Project Structure

```
Go-Back-N-Protocol-Simulator/
│── main.py
└── README.md
```

---

## How to Run

### Clone the Repository

```bash
git clone https://github.com/anjalipandey95/Go-Back-N-Protocol-Simulator.git
```

### Go to Project Folder

```bash
cd Go-Back-N-Protocol-Simulator
```

### Run the Program

```bash
python3 main.py
```



## Sample Input

```
Enter Total Packets : 8
Enter Window Size   : 4
Use Random Packet Loss? (y/n): n
Enter Lost Packet (-1 for no loss): 2
```

---

## Sample Output

```
Packet 2 Lost
Timeout Occurred
Go Back To Packet 2
Retransmitting...

Transmission Completed Successfully
```

---

## Learning Outcomes

This project demonstrates:

- Sliding Window Protocol
- Reliable Data Transmission
- Packet Loss Handling
- Timeout Mechanism
- ACK Handling
- Go-Back-N Retransmission
- Network Protocol Simulation



## Future Enhancements

- Graphical User Interface (GUI)
- Multiple Packet Loss Support
- Network Delay Simulation
- Packet Corruption Simulation
- Selective Repeat Protocol
- Performance Graphs

---

#Author

**Anjali Pandey**

B.Tech (Information Technology)



##License

This project is developed for educational and academic purposes.
