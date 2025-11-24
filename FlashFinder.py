# A script to enumerate memory for a CFI bus
# Created by Zetier
# Drop a star
import sys

def main() -> None:
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <start_addr> <end_addr> <size> <width>")
        sys.exit(1)
    with open("FlashFinder.cmm", "w") as f:
        f.write("area")
        f.write("GLOBALON error continue\n")
        f.write("Flash.list")
        for addr in range(int(sys.argv[1], 16), int(sys.argv[2], 16), int(sys.argv[3], 16)):
            f.write(f"flash.cfi 0x{addr:X} {sys.argv[4]}\n")
    print("Output .cmm file")

if __name__ == "__main__":
    main()