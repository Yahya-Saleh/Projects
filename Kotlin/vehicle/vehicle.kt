fun main() {
    var truck = Truck("KYU146", 2, 350)
    truck.startEngine()
    truck.drive()
    truck.displayInfo()
}

abstract class Vehicle(val _plate_num: String, val _seats: Int) {
    // Properities
    var plate_num: String
    var seats: Int

    // Intializer block
    init {
        plate_num = _plate_num
        seats = _seats
    }

    // Member function
    abstract fun displayInfo()
}

interface VehicleDelegate {
    // Member function
    fun drive()
    fun startEngine()
}

class Truck(_plate_num: String, _seats: Int, _back_size: Int) :
        Vehicle(_plate_num, _seats), VehicleDelegate {
    // Properities
    var back_size: Int

    // Intializer block
    init {
        back_size = _back_size
    }

    override fun displayInfo() {
        println("Card plate number: ${plate_num}")
        println("Seats: ${seats}")
        println("Back size: ${back_size}")
    }

    override fun drive() {
        println("Driving")
    }

    override fun startEngine() {
        println("Starting engine")
    }
}
