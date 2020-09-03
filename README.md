This project references https://github.com/p4lang/tutorials. 
Especially the basic function is modified from https://github.com/p4lang/tutorials/tree/master/exercises/basic
The functions identifying packets by length and time are added by us. 

1. In your shell, run:
   ```bash
   make run
   ```
   This will:
   * compile `basic.p4`, and
   * start the pod-topo in Mininet and configure all switches with
   the appropriate P4 program + table entries, and
   * configure all hosts with the commands listed in
   [pod-topo/topology.json](./pod-topo/topology.json)

2. You should now see a Mininet command prompt. Open two terminals for h1 h2:
   ```bash
   mininet> xterm h1 h2
   ```
3. In h2's XTerm, start the server that captures packet
  ```bash
   ./receive.py
  ```
4. In h1's XTerm, send packets to h2 using send.py
  ```bash
   ./send.py 10.0.2.2 "p4 is cool!"
  ```
5. We can see that in h1's XTerm, the IP.tos=0, while in h2's XTerm, the IP.tos is set to different value according to the length and packet interval time. 

6. Type `exit` to leave each xterm and the Mininet command line.
   Then, to stop mininet:
   ```bash
   make stop
   ```
   And to delete all pcaps, build files, and logs:
   ```bash
   make clean
   ```

