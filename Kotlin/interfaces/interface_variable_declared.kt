interface MyInterface {

    // property with implementation
    val prop: Int
        get() = 23
}

class InterfaceImp : MyInterface {
    // class body
}

fun main(args: Array<String>) {
    val obj = InterfaceImp()

    println(obj.prop)
}
