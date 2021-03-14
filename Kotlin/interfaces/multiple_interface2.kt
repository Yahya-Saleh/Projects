interface A {

    fun callMe() {
        println("From interface A")
    }
}

interface B  {
    fun callMe() {
        println("From interface B")
    }
}

class C: A, B {
    override fun callMe() {
        super<A>.callMe()
        super<B>.callMe()
    }
}

fun main(args: Array<String>) {
    val obj = C()

    obj.callMe()
}