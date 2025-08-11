from config import pt
#====This is for Debugging

#Uncomment one of these to run or not to run the debug
DEBUG = False
# DEBUG = True

#Debugging lines

#For EntryList
def debugEntry(entry, task, uid, i, entries):
    if DEBUG:
        pt("[DEBUG]")
        #----------SHOWING ALL INDEX BEING INDEXED AND THE VALUE-----------
        #USE THIS ONE TO CHECK IF ALL INDEX ACTUALLY INDEXING SOMTHING WE WANT, NOT BLANK
        for i, entry in enumerate(entries):
            print(f"Index i = {i}, Entry #{i + 1}")
            print(f"{entry}")
            
        #--------TO SHOW TOTAL VALID ENTRIES BEING INDEXED--------------
        # print(f"\n📊 Total valid entries: {len(entries)}\n")

        #--------THESE BELOW ARE BS, DON'T USE LOL
        # print(f"\n📦 Entry #{i + 1} (index i = {i})\n{entry}\n")

           
        # print(f"\n[DEBUG] Raw entry:\n{entry}")
        # print(f"[DEBUG] Extracted → Task: {task}, ID: {uid}")
    
        # print(f"\nIndex i = {i}, Entry #{i + 1}\n")
#EOL EntryList        

#For main
def mainDebug():
    return
#EOL main
