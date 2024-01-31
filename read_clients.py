def main():
    infile = open('clients.txt', 'r')
    clientNo = 0

    for client in infile:
        cleintNo += 1
        client = client.rstrip('\n')
        print(f"{clientNo}. {client}")

    print(f"Total number of clients: {clientNo}")
        
        
main() 


