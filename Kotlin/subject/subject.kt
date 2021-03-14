fun main() {
    var score = 43

    if (score < 0) {
        println("Enter a valid number")
    } else {
        print("Based on your score of $score we recommend ")
        when {
            score < 50 -> println("retaking the test")
            score in 50..100 -> println("a Business related subject")
            score in 101..130 -> println("Art and literatures")
            score > 130 -> println("Engineering and Technology")
        }
    }
}
