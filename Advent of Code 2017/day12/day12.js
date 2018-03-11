// Run using node.

let readline = require('readline').createInterface({
    input: require('fs').createReadStream('input.txt')
});

/**
 * Converts input text into pipe representation.
 */
function parseLine(line) {
    let split = line.split(" <-> ");
    
    return {
        from: parseInt(split[0].trim()), 
        to: new Set(split[1].split(",").map(s => parseInt(s.trim())))
    }
}

const adjacenyList = {}

function addPipe(pipe) {
    var currentNeighbours = adjacenyList[pipe.from]

    // if set exists already union with new data, else insert first time.
    adjacenyList[pipe.from] = currentNeighbours ?
        new Set([...currentNeighbours], [...pipe.to]) : pipe.to
}


function traverseComponent(start) {
    // Start at vertex zero and breadth first search to compute diameter.
    let bfsQueue = []
    let nodesDist = { }

    nodesDist[start] = 0

    function visit(node) {
        let curDist = nodesDist[node]

        adjacenyList[node].forEach(neighbour => {
            if (nodesDist[neighbour] >= 0) return;

            nodesDist[neighbour] = curDist+1
            bfsQueue.push(neighbour)
        })
    }

    // Need to initalise the search.
    adjacenyList[start].forEach(neighbour => {
        nodesDist[neighbour] = 1
        bfsQueue.push(neighbour)
    })

    while (bfsQueue.length > 0) {
        visit(bfsQueue.shift())
    }

    return nodesDist;
}

function countSizeOfGroup0() {
    console.log("Answer to part 1:", Object.keys(traverseComponent(0)).length) 
}

function countConnectedComponents() {
    let allNodes = Object.keys(adjacenyList)
    let total = 0;

    while (allNodes.length > 0) {
        let keyToExplore = allNodes.pop();
        let keysToRemove = traverseComponent(keyToExplore)

        allNodes = allNodes.filter(key => !(key in keysToRemove))
        total++
    }

    console.log("Answer to part 2:", total)
}

readline
    .on('line', line => addPipe(parseLine(line)))
    .on('close', () => countSizeOfGroup0())
    .on('close', () => countConnectedComponents())