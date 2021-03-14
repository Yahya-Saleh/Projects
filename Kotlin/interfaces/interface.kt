interface MyInterface {

    val test: Int // abstract property

    fun foo(): String // abstract method (returns String)
    fun hello() { // method with default implementation
        // body (optional)
    }
}

class InterfaceImp : MyInterface {

    override val test: Int = 25
    override fun foo() = "Lol"

    // other code
}
