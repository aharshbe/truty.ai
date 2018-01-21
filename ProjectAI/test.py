import blockchain

msg = """
                Menu:
                        - add message to the existing block.............(1)
                        - show a block (block position will be asked)...(2)
                        - show the whole chain..........................(3)
                        - validate the chain integrity..................(4)

                Note: Any button outside of the menu will exit the program. The validate action will kill the program if the integrity if the chain
                is compromised.
                """

print(msg)
while True:
        print()

        decide = input("Please choose an option: ")

        if decide == "1":
                block.add_message(blockchain.Message(input("Enter your data in the current block:")))
                if len(block.messages) > 0:
                        chain.add_block(block)
                        block = Block()
                else: print("Block is empty, try adding some messages")
        elif decide == "2":
                index = int(input("Provide the box index: "))
                if len(chain.chain) > 0:
                        try: print(chain.chain[index].messages)
                        except: print("The block does not exist at this location.")
        elif decide == "3":
                for b in chain.chain:
                        print(b)
                        print("----------------")
        elif decide == "4":
                if chain.validate(): print("Integrity validated.")
        else:
                break
if __name__ == "__main__":
        manager()