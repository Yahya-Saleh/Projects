fun main() {
    print(salary(100000))
}

fun salary(sales_amount: Int, monthly_salary: Int = 1500) = monthly_salary + sales_amount * 0.02

