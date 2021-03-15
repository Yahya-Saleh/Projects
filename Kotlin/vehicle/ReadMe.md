# Vehicle

A definition for a Truck class that's based on the Vehicle abstract class and its interface.

## Execution

```kotlin
fun main() {
    var truck = Truck("KYU146", 2, 350)
    truck.startEngine()
    truck.drive()
    truck.displayInfo()
}
```

```bash
Starting engine
Driving
Card plate number: KYU146
Seats: 2
Back size: 350
```
