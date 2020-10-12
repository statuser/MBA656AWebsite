from FunctionsAssignment import moving_average as mv_avg
import FunctionsAssignment

important_numbers = list(range(1, 1000))

mv_average = mv_avg(important_numbers, 7)
print(FunctionsAssignment.mean(important_numbers))

print(mv_average)