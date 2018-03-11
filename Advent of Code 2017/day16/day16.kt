import java.io.File

fun <T> swap(arr: Array<T>, A: Int, B: Int) {
    arr[B] = (arr[A]).also { arr[A] = arr[B] }
}

sealed class Instruction {
    abstract fun apply(state: Array<Char>)

    class Spin(private val n: Int): Instruction() {
        override fun apply(state: Array<Char>) {
            val last = state.drop(state.size-n)

            for (i in (state.size-1) downTo n) {
                state[i] = state[i-n]
            }

            for (i in 0..(last.size-1)) {
                state[i] = last[i]
            }
        }
    }

    class Exchange(private val A: Int, private val B: Int) : Instruction() {
        override fun apply(state: Array<Char>) = swap(state, A, B)
    }

    class Partner(private val A: Char, private val B: Char) : Instruction() {
        override fun apply(state: Array<Char>) = swap(
                state, state.indexOf(A), state.indexOf(B)
        )
    }

    companion object {
        private fun createSpin(raw: String): Instruction
                = Instruction.Spin(raw.toInt())

        private fun createExchange(raw: String): Instruction {
            val (a, b) = raw.split("/")

            return Instruction.Exchange(a.toInt(), b.toInt())
        }

        private fun createPartner(raw: String): Instruction {
            val (a, b) = raw.split("/")

            return Instruction.Partner(a.single(), b.single())
        }

        fun from(raw: String): Instruction {
            val payload = raw.substring(1)
            return when {
                raw.startsWith("s") -> createSpin(payload)
                raw.startsWith("x") -> createExchange(payload)
                raw.startsWith("p") -> createPartner(payload)
                else -> throw Exception("didn't recognise instruction $raw")
            }
        }
    }
}

fun readInput(file: String): List<Instruction> {
    return File(file).readText()
            .split(",")
            .map({ Instruction.from(it) })
}

fun runSimulation(n: Int, instructions: List<Instruction>): Array<Char> {
    val letters = Array(n, {i -> (97+i).toChar()})

    instructions.forEach( {it.apply(letters)} )

    return letters
}

fun main(args: Array<String>) {
    val instructions = readInput("input.txt")

    val simulation = runSimulation(16, instructions)

    // To perform the dance 1_000_000_000 we'll keep the dance until
    // we hopefully discover a cycle and then we can just use memoization
    val states = mutableListOf(simulation.joinToString(""))

    for (i in 2..1_000_000_000) {
        instructions.forEach({it.apply(simulation)})

        val newSim = simulation.joinToString("")

        if (states.contains(newSim)) {
            // Every 'i' iterations get's back to the same place
            // So every 10^9%i wil be the actually affected states
            val x = 1_000_000_000%(i-1)

            println("After a bil we got: ${states[x-1]}")
            return
        }
        states.add(newSim)
    }

}