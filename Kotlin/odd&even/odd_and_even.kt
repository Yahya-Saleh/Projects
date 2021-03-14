fun main() {
    val numbers = Array(10, { i -> i + 1 })

    var even = 0
    var odd = 0

    for (num in numbers) {
        if (num % 2 == 0) {
            even++
        } else {
            odd++
        }
    }

    println("${odd} odd number(s) and ${even} even number(s)")
}
