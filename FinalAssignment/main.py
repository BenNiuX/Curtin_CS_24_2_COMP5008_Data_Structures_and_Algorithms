from DSAGraph import DSAGraph
from DSAHashTable import DSAHashTable
from DSAVehicle import Vehicle
from DSAsorts import findNearestVehicle, findVehicleWithHighestBattery

OPTIONS = [
    'gav', 'gdv', 'gae', 'gde', 'grn', 'gdg', 'gcp',
    'hi', 'hr', 'hs', 'hd',
    'rnv', 'rhb',
    'q']
OPTION_DESCS = [
    "Graph: Add Vertex",  # 0
    "Graph: Delete Vertex",  # 1
    "Graph: Add Edge",  # 2
    "Graph: Delete Edge",  # 3
    "Graph: Retrieve Neighbors",  # 4
    "Graph: Display Graph",  # 5
    "Graph: Check Path",  # 6
    "HashTable: Insert",  # 7
    "HashTable: Remove",  # 8
    "HashTable: Search",  # 9
    "HashTable: Display",  # 10
    "Recommend: Nearest Vehicle",  # 11
    "Recommend: Highest Battery",  # 12
    "Quit"  # 13
]


def usage():
    """
    Print the usage of the interactive menu.
    """
    print("\r\n==================================")
    print("Interactive Menu for DSA Assignment")
    for i, opt in enumerate(OPTIONS):
        print(f"  ({opt}) {OPTION_DESCS[i]}")
    print("==================================\r\n")


def interactive():
    """
    Interactive menu for the DSA assignment.
    """
    usage()
    userInput = ''
    graph = DSAGraph(DSAGraph.UNDIRECTED)
    hashTable = DSAHashTable(10)
    while userInput != OPTIONS[-1]:
        userInput = input(f"\r\nPlease input options: {', '.join(OPTIONS)}: ")
        if userInput == OPTIONS[0]:
            item = input("\nPlease input the vertex label: ")
            try:
                graph.addVertex(item)
            except ValueError as e:
                print('Error happened', e, 'Please try again')
        elif userInput == OPTIONS[1]:
            item = input("\nPlease input the vertex label: ")
            try:
                graph.deleteVertex(item)
                print(f"Delete node: '{item}' success")
            except ValueError as e:
                print('Error happened', e, 'Please try again')
        elif userInput == OPTIONS[2]:
            item = input("\nPlease input the edge like LABEL1 LABEL2 DISTANCE: ")
            items = item.split()
            if len(items) == 3:
                try:
                    graph.addEdge(items[0], items[1], int(items[2]))
                except ValueError as e:
                    print('Error happened', e, 'Please try again')
            else:
                print("Input error")
        elif userInput == OPTIONS[3]:
            item = input("\nPlease input the edge like LABEL1 LABEL2: ")
            items = item.split()
            if len(items) == 2:
                try:
                    graph.deleteEdge(items[0], items[1])
                    print(f"\nDelete edge: {items[0]}-{items[1]} success")
                except ValueError as e:
                    print('Error happened', e, 'Please try again')
            else:
                print("Input error")
        elif userInput == OPTIONS[4]:
            item = input("\nPlease input the vertex label: ")
            if not graph.hasVertex(item):
                print("Input error")
            else:
                adjList = graph.getAdjacent(item)
                if adjList:
                    node = adjList.head
                    neis = []
                    while node is not None:
                        neis.append(node.value.label)
                        node = node.next
                    print(f"\n{item} neighbors: {', '.join(neis)}")
                else:
                    print(f"{item} has no neighbors")
        elif userInput == OPTIONS[5]:
            graph.sort()
            graph.displayAsMatrix()
            graph.displayAsList()
            graph.displayEdges()
        elif userInput == OPTIONS[6]:
            item = input("\nPlease input the vertex like LABEL1 LABEL2: ")
            items = item.split()
            if len(items) == 2:
                if graph.isPath(items[0], items[1]):
                    print(f"\nThere is a path from {items[0]} to {items[1]}")
                else:
                    print(f"\nThere is no path from {items[0]} to {items[1]}")
        elif userInput == OPTIONS[7]:
            item = input(
                "\nPlease input the vehicle info like"
                + " ID CurLoc DestLoc BatteryLevel: "
            )
            items = item.split()
            if len(items) == 4:
                vid = items[0]
                curLoc = items[1]
                destLoc = items[2]
                if graph.getVertex(curLoc) is None or graph.getVertex(destLoc) is None:
                    print("Input location error")
                    continue
                try:
                    batteryLevel = int(items[3])
                except ValueError:
                    print("Input battery level error")
                    continue
                veh = Vehicle(vid)
                veh.setLocation(curLoc)
                veh.setDestination(destLoc)
                veh.setBatteryLevel(batteryLevel)
                veh.setDistanceToDest(graph.getDistance(curLoc, destLoc))
                try:
                    hashTable.insert(veh)
                except KeyError as e:
                    print('Error happened', e, 'Please try again')
            else:
                print("Input error")
        elif userInput == OPTIONS[8]:
            item = input("\nPlease input the vehicle ID: ")
            if hashTable.delete(item):
                print(f"\nDelete vehicle: {item} success")
            else:
                print("Input error")
        elif userInput == OPTIONS[9]:
            item = input("\nPlease input the vehicle ID: ")
            veh = hashTable.search(item)
            if veh:
                print(f"\nFind vehicle: {veh}")
            else:
                print("Input error")
        elif userInput == OPTIONS[10]:
            hashTable.display()
        elif userInput == OPTIONS[11]:
            vehArrary = hashTable.export()
            veh = findNearestVehicle(vehArrary)
            print(f"\nNearest vehicle: {veh}")
        elif userInput == OPTIONS[12]:
            vehArrary = hashTable.export()
            veh = findVehicleWithHighestBattery(vehArrary)
            print(f"\nHighest battery level vehicle: {veh}")
        elif userInput == OPTIONS[-1]:
            print("\n!!!BYE BYE!!!")
        else:
            usage()


if __name__ == "__main__":
    interactive()
