fun main() {
    val myFirstDice = Dice(6)
    println("The ${myFirstDice.numSides} sided dice rolled ${myFirstDice.roll()}!")

    val mySecondDice = Dice(20)
    println("The ${mySecondDice.numSides} sided dice rolled ${mySecondDice.roll()}!")
}

class Dice(val numSides: Int) {

    fun roll(): Int {
        return (1..numSides).random()
    }
}
