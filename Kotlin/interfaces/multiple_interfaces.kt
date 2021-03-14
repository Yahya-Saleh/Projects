interface A {

    fun callMe() {
        println("From interface A")
    }
}

interface B {
    fun callMeToo() {
        println("From interface B")
    }
}

// implements two interfaces A and B
class Child : A, B

fun main(args: Array<String>) {
    val obj = Child()

    obj.callMe()
    obj.callMeToo()
}
