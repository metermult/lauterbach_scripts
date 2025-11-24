# Lauterbach Scripts

## Warning

There are possibilities that the following scripts WILL PERMANENTLY brick your systems. We have tried some of these scripts in the past and it is extremely important to know how these scripts work through outside research. It is entirely possible to write to a flash controller and wipe memory or kick data out to a peripheral that renders it a potato. Please exercise these scripts with caution. 

## 1. FlashFinder 

FlashFinder is a tool to enumerate memory of a processor for a common flash interface (CFI) bus. It will walk across memory from 0x0 (or specified start address) to end address using the provided minimum flash size. This tool is especially useful for processors that have a changable memory map or multiple memory regions. Flash must be CFI compliant for this tool to work. Flash attributes such as size and addresses must be in hex. 

To run the tool simply: 
```
python3 FlashFinder.py [start_address] [end_address] [flash_size] [width]
```
Example: python3 FlashFinder.py 0x0 0xffffffff 0x40000 long

The last parameter can be byte, long, word, dword, or qword. 

After running the python script, a `.cmm` script will be produced to run with Lauterbach by using the `DO` command. This will enumerate every interval for the flash memory. When a CFI bus is found, the `flash.list` window will be populated with data. 