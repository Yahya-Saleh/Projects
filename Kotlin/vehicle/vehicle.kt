fun main() {
    val veh = Vehicle("APR 127", 4)
    veh.displayInfo()
}

class Vehicle(val _plate_num: String, val _seats: Int) {
    // Properities
    var plate_num: String
    var seats: Int

    // Intializer block
    init {
        plate_num = _plate_num
        seats = _seats
    }

    // Member function
    fun displayInfo() {
        println("Card plate number: ${plate_num}")
        println("Seats: ${seats}")
    }
}
